import os
import boto3
from botocore.exceptions import NoCredentialsError
import hashlib
from .config_manager import ConfigManager

config = ConfigManager.get_config()

config = ConfigManager.get_config()

def calculate_directory_hash(directory):
    hash_obj = hashlib.sha256()
    for root, dirs, files in os.walk(directory):
        for file in sorted(files):
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_obj.update(chunk)
    return hash_obj.hexdigest()

def upload_data_to_s3():
    session = boto3.Session(
        aws_access_key_id=config['aws']['access_key_id'],
        aws_secret_access_key=config['aws']['secret_access_key']
    )
    s3 = session.client('s3')
    hash_file_path = os.path.join(config['data_directory'], '.hash')
    current_hash = calculate_directory_hash(config['data_directory'])
    
    # Check if hash is different
    if os.path.exists(hash_file_path):
        with open(hash_file_path, 'r') as file:
            if file.read().strip() == current_hash:
                return  # No changes, no upload needed
    
    try:
        for root, dirs, files in os.walk(config['data_directory']):
            for file in files:
                s3.upload_file(os.path.join(root, file), config['aws']['s3_bucket'],
                               config['aws']['s3_data_key'] + file)
        with open(hash_file_path, 'w') as file:
            file.write(current_hash)  # Update the hash
    except NoCredentialsError as e:
        logging.error(f"AWS credentials not found: {e}")
    except Exception as e:
        logging.error(f"Unexpected error during S3 upload: {e}")

def download_data_directory():
    session = boto3.Session(
        aws_access_key_id=config['aws']['access_key_id'],
        aws_secret_access_key=config['aws']['secret_access_key']
    )
    s3 = session.client('s3')
    local_directory = config['data_directory']
    os.makedirs(local_directory, exist_ok=True)
    # Assuming bucket directory is data/
    for obj in s3.list_objects(Bucket=config['aws']['s3_bucket'], Prefix=config['aws']['s3_data_key'])['Contents']:
        path, filename = os.path.split(obj['Key'])
        s3.download_file(config['aws']['s3_bucket'], obj['Key'], os.path.join(local_directory, filename))

def generate_presigned_url(file_key):
    session = boto3.Session(
        aws_access_key_id=config['aws']['access_key_id'],
        aws_secret_access_key=config['aws']['secret_access_key']
    )
    s3 = session.client('s3')
    try:
        response = s3.generate_presigned_url('get_object',
                                             Params={'Bucket': config['aws']['s3_bucket'],
                                                     'Key': config['aws']['s3_diagram_key'] + file_key},
                                             ExpiresIn=config['url_expiry'])
        return response
    except Exception as e:
        print(f"Error generating presigned URL: {e}")
        return None
    except NoCredentialsError as e:
        logging.error(f"AWS credentials not found: {e}")
    except Exception as e:
        logging.error(f"Unexpected error during S3 operation: {e}")
