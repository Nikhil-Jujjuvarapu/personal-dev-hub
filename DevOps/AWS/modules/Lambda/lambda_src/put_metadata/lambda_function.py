import json
import boto3
from botocore.exceptions import ClientError

# Initialize AWS clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')  # Replace with your table name

def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event['body'])
        print(body)
        bucket_name = body.get('bucket_name')
        object_key = body.get('object_key')

        if not bucket_name or not object_key:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing bucket_name or object_key"})
            }

        # Fetch object metadata from S3
        try:
            response = s3.head_object(Bucket=bucket_name, Key=object_key)
        except ClientError as e:
            return {
                "statusCode": 403 if e.response['Error']['Code'] == 'AccessDenied' else 404,
                "body": json.dumps({"error": str(e)})
            }

        # Prepare item to store in DynamoDB
        item = {
            "file_name": object_key,
            "bucket_name": bucket_name,
            "size": response['ContentLength'],
            "content_type": response['ContentType'],
            "last_modified": response['LastModified'].isoformat()
        }

        # Store metadata in DynamoDB
        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Metadata stored successfully", "item": item})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
