Root module

This folder contains a small root Terraform module that instantiates the project modules:

- `module.lambda` -> `../modules/Lambda`
- `module.s3`     -> `../modules/S3`

It wires the Lambda module's `lambda_exec_role_arn` output into the S3 module via the `lambda_role_arn` variable.

Usage (from PowerShell):

```powershell
cd AWS/root
terraform init
terraform plan -var-file="../envs/dev/dev.tfvars"
```

If you keep your environment tfvars in another location, pass appropriate `-var` or `-var-file` values.
