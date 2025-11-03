terraform {
  backend "s3" {
    bucket         = "imaginary-vault-bucket"
    key            = "tflock/dev/dynamoDb/terraform.tfstate"  # Lambda's specific state path
    region         = "ap-south-1"
    encrypt        = true
  }
}