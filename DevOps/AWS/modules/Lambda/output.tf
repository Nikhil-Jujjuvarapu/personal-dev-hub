output "lambda_exec_role_arn" {
  value       = aws_iam_role.lambda_exec_role.arn
  description = "ARN of the lambda execution role"
}

output "get_metadata_invoke_arn" {
  value       = aws_lambda_function.get_metadata.invoke_arn
  description = "Invoke ARN for the GET metadata Lambda function"
}

output "put_metadata_invoke_arn" {
  value       = aws_lambda_function.put_metadata.invoke_arn
  description = "Invoke ARN for the PUT metadata Lambda function"
}

output "get_metadata_function_name" {
  value       = aws_lambda_function.get_metadata.function_name
  description = "Function name of the GET metadata Lambda"
}

output "put_metadata_function_name" {
  value       = aws_lambda_function.put_metadata.function_name
  description = "Function name of the PUT metadata Lambda"
}