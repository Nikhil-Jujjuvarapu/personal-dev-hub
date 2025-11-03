variable "account_id" {}
variable "iam_user_name" {}
variable "region" {}
variable "bucket_name" {}
variable "s3_lambda_fn_name" {}



variable "table_name" {
  description = "DynamoDB table name for image metadata"
  type        = string
  default     = "ImageMetadata"  # PascalCase for table names
}