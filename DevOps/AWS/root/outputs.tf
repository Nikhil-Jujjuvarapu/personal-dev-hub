

# output "bucket_name" {
#   value       = var.bucket_name
#   description = "Configured S3 bucket name"
# }


# output "cognito_user_pool_arn" {
#   value       = aws_cognito_user_pool.app_pool.arn
#   description = "user pool arn"
# }

# output "user_pool_id" {
#   description = "The ID of the Cognito User Pool"
#   value       = aws_cognito_user_pool.app_pool.id
# }

# output "user_pool_client_id" {
#   description = "The ID of the Cognito App Client"
#   value       = aws_cognito_user_pool_client.app_client.id
# }
# output "table_name" {
#   description = "DynamoDB table name"
#   value       = aws_dynamodb_table.image_metadata.name
# }

# output "table_arn" {
#   description = "DynamoDB table ARN"
#   value       = aws_dynamodb_table.image_metadata.arn
# }

# output "table_id" {
#   description = "DynamoDB table ID"
#   value       = aws_dynamodb_table.image_metadata.id
# }

# output "api_gateway_exec_role_arn" {
#   value       = aws_iam_role.api_gateway_cloudwatch_role.arn
#   description = "ARN of the apigateway execution role"
# }

# output "lambda_exec_role_arn" {
#   value       = aws_iam_role.lambda_exec_role.arn
#   description = "ARN of the lambda execution role"
# }

# output "get_metadata_invoke_arn" {
#   value       = aws_lambda_function.get_metadata.invoke_arn
#   description = "Invoke ARN for the GET metadata Lambda function"
# }

# output "put_metadata_invoke_arn" {
#   value       = aws_lambda_function.put_metadata.invoke_arn
#   description = "Invoke ARN for the PUT metadata Lambda function"
# }

# output "get_metadata_function_name" {
#   value       = aws_lambda_function.get_metadata.function_name
#   description = "Function name of the GET metadata Lambda"
# }

# output "put_metadata_function_name" {
#   value       = aws_lambda_function.put_metadata.function_name
#   description = "Function name of the PUT metadata Lambda"
# }