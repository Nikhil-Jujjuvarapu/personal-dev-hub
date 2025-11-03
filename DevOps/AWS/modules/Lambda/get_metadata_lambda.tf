

data "archive_file" "lambda_get_metadata_zip" {
  type        = "zip"
  source_file = "${path.module}/lambda_src/get_metadata/lambda_function.py"
  output_path = "${path.module}/lambda_src/get_metadata/lambda_function.zip"
}

resource "aws_lambda_function" "get_metadata" {
  function_name = var.get_metadata_fn
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  filename      = data.archive_file.lambda_get_metadata_zip.output_path
  memory_size = 128
  timeout     = 20
  source_code_hash = data.archive_file.lambda_get_metadata_zip.output_base64sha256
}

resource "aws_cloudwatch_log_group" "lambda_get_metadata_log_group" {
  name              = "/aws/lambda/${aws_lambda_function.get_metadata.function_name}"
  retention_in_days = 14
  
}

