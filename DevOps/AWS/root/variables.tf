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
