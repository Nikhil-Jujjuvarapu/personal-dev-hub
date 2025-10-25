#Bucket creation
resource "aws_s3_bucket" "personal" {
  bucket = var.bucket_name
  region = var.region
  

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}


# block public access
resource "aws_s3_bucket_public_access_block" "block_public_block" {
  bucket = aws_s3_bucket.personal.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

data "terraform_remote_state" "lambda" {
  backend = "s3"
  config = {
    bucket = "imaginary-vault-bucket"
    # Must match the Lambda's key exactly
    key    = "tflock/dev/lambda/terraform.tfstate" 
    region = "ap-south-1"
  }
}
locals {
  # Assign the remote state output value to a clear local variable
  lambda_role_arn_ref = data.terraform_remote_state.lambda.outputs.lambda_exec_role_arn
}

# Bucket policy to allow only your IAM user
resource "aws_s3_bucket_policy" "personal_access" {
  bucket = aws_s3_bucket.personal.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowMyUserOnly"
        Effect    = "Allow"
        Principal = {
          AWS = ["arn:aws:iam::${var.account_id}:user/${var.iam_user_name}",
          local.lambda_role_arn_ref
          ]
        }
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.personal.arn,
          "${aws_s3_bucket.personal.arn}/*"
        ]
      },
      {
        Sid      = "DenyEveryoneElse"
        Effect   = "Deny"
        Principal = "*"
        Action   = "s3:*"
        Resource = [
          aws_s3_bucket.personal.arn,
          "${aws_s3_bucket.personal.arn}/*"
        ]
        Condition = {
          StringNotEquals = {
            "aws:PrincipalArn" = ["arn:aws:iam::${var.account_id}:user/${var.iam_user_name}",
            local.lambda_role_arn_ref
            ]
          }
        }
      }
    ]
  })
}
