


# DynamoDB Table
resource "aws_dynamodb_table" "image_metadata" {
  name           = var.table_name
  billing_mode   = "PROVISIONED"
  hash_key       = "file_name"  # snake_case for attribute names
  read_capacity  = 5
  write_capacity = 5

  attribute {
    name = "file_name"
    type = "S"
  }

  tags = {
    Name        = var.table_name
    Environment = "DEV"
    ManagedBy   = "Terraform"
  }
}

