

data "archive_file" "lambda_post_metadata_zip" {
  type        = "zip"
  source_file = "${path.module}/lambda_src/put_metadata/lambda_function.py"
  output_path = "${path.module}/lambda_src/put_metadata/lambda_function.zip"
}

resource "aws_lambda_function" "put_metadata" {
  function_name = var.put_metadata_fn
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  filename      = data.archive_file.lambda_post_metadata_zip.output_path
  memory_size = 128
  timeout     = 20
  source_code_hash = data.archive_file.lambda_post_metadata_zip.output_base64sha256
}

resource "aws_cloudwatch_log_group" "lambda_put_metadata_log_group" {
  name              = "/aws/lambda/${aws_lambda_function.put_metadata.function_name}"
  retention_in_days = 14
  
}

