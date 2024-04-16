import os
import boto3
from botocore.exceptions import NoCredentialsError
import hashlib
import yaml

from app.config import load_config

config = load_config()

def calculate_directory_hash(directory):
    hash_obj = hashlib.sha256()
    for root, dirs, files in os.walk(directory):
        for file in sorted(files):
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_obj.update(chunk)
    return hash_obj.hexdigest()

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
