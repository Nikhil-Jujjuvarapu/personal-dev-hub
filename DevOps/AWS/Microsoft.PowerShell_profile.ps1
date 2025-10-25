function tfdev {
    param(
        [Parameter(Mandatory=$true)]
        [string]$command
    )
    # The -Force ensures the apply continues when input is false
    terraform $command -var-file="envs/dev/dev.tfvars" $args
}