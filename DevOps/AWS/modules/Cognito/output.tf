output "cognito_user_pool_arn" {
  value       = aws_cognito_user_pool.app_pool.arn
  description = "user pool arn"
}

output "user_pool_id" {
  description = "The ID of the Cognito User Pool"
  value       = aws_cognito_user_pool.app_pool.id
}

output "user_pool_client_id" {
  description = "The ID of the Cognito App Client"
  value       = aws_cognito_user_pool_client.app_client.id
}