S3 bucket - imaginary-vault-bucket

DynamoDb Table Creation - 

ImageData - Table name
partition key - file_name
column names - file name, size, content type, last modified

Api Gateway - 
REST API -

image-metadata -
	POST - /images
	GET  - /images/file_name
	
lambda -
	get and post based on request from api gateway
	dynamodb connectivity

IAM Roles - add to existing roles

cloudwatch - add metric filter