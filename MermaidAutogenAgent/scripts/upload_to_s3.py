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
            if file.read() == current_hash:
                return  # No changes, no upload needed
    
    try:
        for root, dirs, files in os.walk(config['data_directory']):
            for file in files:
                s3.upload_file(os.path.join(root, file), config['aws']['s3_bucket'],
                               config['aws']['s3_data_key'] + file)
        with open(hash_file_path, 'w') as file:
            file.write(current_hash)  # Update the hash
    except NoCredentialsError:
        print("AWS credentials not found.")
