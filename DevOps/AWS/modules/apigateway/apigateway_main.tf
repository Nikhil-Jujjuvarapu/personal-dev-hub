# Create the API Gateway
resource "aws_api_gateway_rest_api" "dev_api" {
  name = var.api_name
  description = "API Gateway for Dev"
}

# Create the /image-data resource
resource "aws_api_gateway_resource" "image_data" {
  rest_api_id = aws_api_gateway_rest_api.dev_api.id
  parent_id   = aws_api_gateway_rest_api.dev_api.root_resource_id
  path_part   = "image-data"
}

# GET method setup
resource "aws_api_gateway_method" "get_method" {
  rest_api_id   = aws_api_gateway_rest_api.dev_api.id
  resource_id   = aws_api_gateway_resource.image_data.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "get_integration" {
  rest_api_id = aws_api_gateway_rest_api.dev_api.id
  resource_id = aws_api_gateway_resource.image_data.id
  http_method = aws_api_gateway_method.get_method.http_method
  
  integration_http_method = "POST"
  type                   = "AWS_PROXY"
  uri                    = data.terraform_remote_state.lambda.outputs.get_metadata_invoke_arn
}

# POST method setup
resource "aws_api_gateway_method" "post_method" {
  rest_api_id   = aws_api_gateway_rest_api.dev_api.id
  resource_id   = aws_api_gateway_resource.image_data.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "post_integration" {
  rest_api_id = aws_api_gateway_rest_api.dev_api.id
  resource_id = aws_api_gateway_resource.image_data.id
  http_method = aws_api_gateway_method.post_method.http_method
  
  integration_http_method = "POST"
  type                   = "AWS_PROXY"
  uri                    = data.terraform_remote_state.lambda.outputs.put_metadata_invoke_arn
}

# Deployment
resource "aws_api_gateway_deployment" "api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.dev_api.id
  
  depends_on = [
    aws_api_gateway_integration.get_integration,
    aws_api_gateway_integration.post_integration
  ]
}

resource "aws_cloudwatch_log_group" "api_gateway_logs" {
  name              = "/aws/apigw/access/${aws_api_gateway_rest_api.dev_api.name}-access"
  retention_in_days = 14
}

resource "aws_api_gateway_account" "api_gateway_account" {
  cloudwatch_role_arn = data.terraform_remote_state.iam.outputs.api_gateway_exec_role_arn
  depends_on = [
    aws_cloudwatch_log_group.api_gateway_logs
  ]
}

# Stage
resource "aws_api_gateway_stage" "api_stage" {
  deployment_id = aws_api_gateway_deployment.api_deployment.id
  rest_api_id  = aws_api_gateway_rest_api.dev_api.id
  stage_name   = var.stage_name
  
  depends_on = [aws_api_gateway_account.api_gateway_account]
  
  # Enable detailed CloudWatch metrics
  xray_tracing_enabled = true
  
  access_log_settings {
      destination_arn = aws_cloudwatch_log_group.api_gateway_logs.arn
      format = jsonencode({
        requestId               = "$context.requestId",
        ip                      = "$context.identity.sourceIp",
        caller                  = "$context.identity.caller",
        user                    = "$context.identity.user",
        requestTime             = "$context.requestTime",
        httpMethod              = "$context.httpMethod",
        resourcePath            = "$context.resourcePath",
        status                  = "$context.status",
        protocol                = "$context.protocol",
        responseLength          = "$context.responseLength",
        responseLatency         = "$context.responseLatency",
        integrationLatency      = "$context.integrationLatency"
      })
    }
}

# Enable CloudWatch logging for all methods
resource "aws_api_gateway_method_settings" "all" {
  rest_api_id = aws_api_gateway_rest_api.dev_api.id
  stage_name  = aws_api_gateway_stage.api_stage.stage_name
  method_path = "*/*"

  depends_on = [aws_api_gateway_account.api_gateway_account]

  settings {
    metrics_enabled        = true
    logging_level         = "INFO"
    data_trace_enabled    = true
    throttling_burst_limit = 100
    throttling_rate_limit  = 100
  }
}

# Lambda permissions for API Gateway
resource "aws_lambda_permission" "api_gateway_get" {
  statement_id  = "AllowExecutionFromAPIGatewayGET"
  action        = "lambda:InvokeFunction"
  function_name = data.terraform_remote_state.lambda.outputs.get_metadata_function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.dev_api.execution_arn}/*/*"
}

resource "aws_lambda_permission" "api_gateway_post" {
  statement_id  = "AllowExecutionFromAPIGatewayPOST"
  action        = "lambda:InvokeFunction"
  function_name = data.terraform_remote_state.lambda.outputs.put_metadata_function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.dev_api.execution_arn}/*/*"
}

# Remote state data source for Lambda
data "terraform_remote_state" "lambda" {
  backend = "s3"
  config = {
    bucket = "imaginary-vault-bucket"
    key    = "tflock/dev/lambda/terraform.tfstate"
    region = "ap-south-1"
  }
}

# Remote state data source for cognito arn
data "terraform_remote_state" "cognito" {
  backend = "s3"

  config = {
    bucket = "imaginary-vault-bucket"
    key    = "tflock/dev/cognito/terraform.tfstate"
    region = "ap-south-1"
  }
}

data "terraform_remote_state" "iam" {
  backend = "s3"

  config = {
    bucket = "imaginary-vault-bucket"
    key    = "tflock/dev/iam/terraform.tfstate"
    region = "ap-south-1"
  }
}


resource "aws_api_gateway_authorizer" "cognito_auth" {
  name                   = "cognito_authorizer"
  rest_api_id            = aws_api_gateway_rest_api.dev_api.id
  type                   = "COGNITO_USER_POOLS"
  # provider_arns          = data.terraform_remote_state.lambda.outputs.cognito_user_pool_arn
  provider_arns   = [data.terraform_remote_state.cognito.outputs.cognito_user_pool_arn]
  identity_source        = "method.request.header.Authorization"
}
