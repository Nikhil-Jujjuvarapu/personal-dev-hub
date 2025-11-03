variable "account_id" {
  description = "AWS account ID"
  type        = string
}

variable "iam_user_name" {
  description = "IAM user name that will be allowed to access the S3 bucket"
  type        = string
}

variable "region" {
  description = "AWS region"
  type        = string
}

variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "s3_lambda_fn_name" {
  description = "Lambda function name used for S3 notifications"
  type        = string
}

variable "get_metadata_fn" {
  description = "Lambda function name for GET metadata"
  type        = string
  default     = "get_metadata_fn"
}

variable "put_metadata_fn" {
  description = "Lambda function name for PUT metadata"
  type        = string
  default     = "put_metadata_fn"
}

variable "table_name" {
  description = "DynamoDB table name"
  type        = string
  default     = "ImageMetadata"
}

variable "api_name" {
  description = "API Gateway name"
  type        = string
  default     = "DEV-API"
}

variable "stage_name" {
  description = "API Gateway stage name"
  type        = string
  default     = "v1"
}

variable "user_pool_name" {
  description = "Cognito user pool name"
  type        = string
  default     = "dev_user_pool"
}

variable "app_client_name" {
  description = "Cognito app client name"
  type        = string
  default     = "dev_app_client"
}
