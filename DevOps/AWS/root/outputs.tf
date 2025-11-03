output "lambda_role_arn" {
  value       = module.lambda.lambda_exec_role_arn
  description = "ARN of the lambda execution role (from Lambda module)"
}

output "bucket_name" {
  value       = var.bucket_name
  description = "Configured S3 bucket name"
}
