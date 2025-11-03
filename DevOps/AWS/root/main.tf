// Root module to wire Lambda and S3 modules together
// Instantiates the Lambda module and passes its role ARN into the S3 module

module "lambda" {
  source           = "../modules/Lambda"

  account_id       = var.account_id
  iam_user_name    = var.iam_user_name
  region           = var.region
  bucket_name      = var.bucket_name
  s3_lambda_fn_name = var.s3_lambda_fn_name
}

module "s3" {
  source           = "../modules/S3"

  account_id       = var.account_id
  iam_user_name    = var.iam_user_name
  region           = var.region
  bucket_name      = var.bucket_name
  s3_lambda_fn_name = var.s3_lambda_fn_name

  # pass the role ARN output from the Lambda module
  lambda_role_arn  = module.lambda.lambda_exec_role_arn
}
