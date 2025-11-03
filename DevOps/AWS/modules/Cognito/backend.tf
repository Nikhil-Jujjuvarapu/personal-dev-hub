terraform {
  backend "s3" {
    bucket         = "imaginary-vault-bucket"
    key            = "tflock/dev/cognito/terraform.tfstate"     
    region         = "ap-south-1"
    encrypt        = true
  }
}