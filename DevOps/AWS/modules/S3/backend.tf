terraform {
  backend "s3" {
    bucket         = "imaginary-vault-bucket"
    key            = "tflock/dev/s3/terraform.tfstate"      # S3's specific state path
    region         = "ap-south-1"
    encrypt        = true
  }
}