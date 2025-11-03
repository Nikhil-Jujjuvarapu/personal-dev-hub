// Root module to wire Lambda and S3 modules together
// Instantiates the Lambda module and passes its role ARN into the S3 module

module "iam" {
  source = "../modules/IAM"

  account_id    = var.account_id
  iam_user_name = var.iam_user_name
  region        = var.region
}

module "s3" {
  source = "../modules/S3"

  account_id       = var.account_id
  iam_user_name    = var.iam_user_name
  region            = var.region
  bucket_name       = var.bucket_name
  s3_lambda_fn_name = var.s3_lambda_fn_name
  lambda_role_arn   = module.lambda.lambda_exec_role_arn
}

module "lambda" {
  source = "../modules/Lambda"

  account_id       = var.account_id
  iam_user_name    = var.iam_user_name
  region           = var.region
  bucket_name      = var.bucket_name
  s3_lambda_fn_name = var.s3_lambda_fn_name
  get_metadata_fn  = var.get_metadata_fn
  put_metadata_fn  = var.put_metadata_fn
  table_name       = var.table_name
}

module "dynamodb" {
  source = "../modules/dynamoDb"

  account_id    = var.account_id
  iam_user_name = var.iam_user_name
  region        = var.region
  bucket_name   = var.bucket_name
  s3_lambda_fn_name = var.s3_lambda_fn_name
  table_name    = var.table_name
}

module "cognito" {
  source = "../modules/Cognito"

  account_id     = var.account_id
  iam_user_name  = var.iam_user_name
  region         = var.region
  bucket_name    = var.bucket_name
  user_pool_name = var.user_pool_name
  app_client_name = var.app_client_name
}

module "apigateway" {
  source = "../modules/apigateway"

  account_id       = var.account_id
  iam_user_name    = var.iam_user_name
  region           = var.region
  bucket_name      = var.bucket_name
  s3_lambda_fn_name = var.s3_lambda_fn_name
  api_name         = var.api_name
  stage_name       = var.stage_name
  lambda_role_arn  = module.lambda.lambda_exec_role_arn
}
