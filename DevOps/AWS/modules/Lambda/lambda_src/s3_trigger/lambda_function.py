import json
import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Extract bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Get object metadata
    response = s3.head_object(Bucket=bucket_name, Key=object_key)

    metadata = {
        "Bucket": bucket_name,
        "FileName": object_key,
        "Size": response['ContentLength'],
        "ContentType": response.get('ContentType', 'N/A'),
        "LastModified": str(response['LastModified']),
        "ETag": response['ETag'],
        "Metadata": response.get('Metadata', {})
    }

    print("File Metadata:")
    print(json.dumps(metadata, indent=4))

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Metadata printed successfully!'})
    }