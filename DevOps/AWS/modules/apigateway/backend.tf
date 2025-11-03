terraform {
  backend "s3" {
    bucket         = "imaginary-vault-bucket"
    key            = "tflock/dev/apigateway/terraform.tfstate"     
    region         = "ap-south-1"
    encrypt        = true
  }
}