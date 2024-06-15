import boto3

def upload_file_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, s3_key)

def download_file_from_s3(bucket_name, s3_key, file_path):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, s3_key, file_path)
