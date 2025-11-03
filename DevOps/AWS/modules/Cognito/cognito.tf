resource "aws_cognito_user_pool" "app_pool" {
  name = var.user_pool_name

  # Enforce strong password policy
  password_policy {
    minimum_length    = 8
    require_lowercase = true
    require_numbers   = true
    require_symbols   = true
    require_uppercase = true
  }

  # Enable email as the primary sign-in attribute (username)
  username_attributes = ["email"]
  
  # Automatically verify the user's email upon signup
  auto_verified_attributes = ["email"]
}

resource "aws_cognito_user_pool_client" "app_client" {
  name         = var.user_pool_name
  user_pool_id = aws_cognito_user_pool.app_pool.id
  
  # Set to false for public clients (like SPAs) - they cannot securely store a secret
  generate_secret = false 

  # Allow users to sign in with email and password flow
  explicit_auth_flows = [ "ALLOW_ADMIN_USER_PASSWORD_AUTH","ALLOW_USER_PASSWORD_AUTH", "ALLOW_REFRESH_TOKEN_AUTH"] 



  # Set the refresh token validity (e.g., 30 days)
  refresh_token_validity = 30
}

