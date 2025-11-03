variable "account_id" {}
variable "iam_user_name" {}
variable "region" {}
variable "bucket_name" {}
variable "s3_lambda_fn_name" {}
variable "api_name" {}
variable "stage_name" {}
variable "lambda_role_arn" {
  type        = string
  description = "ARN of the lambda execution role (passed from lambda module)"
  default     = null
}
