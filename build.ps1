docker buildx build --platform=linux/arm64,linux/amd64 -t jxch/capital-ds3:$(Get-Date -Format 'yyyy-MM-dd') -t jxch/capital-ds3:latest . --push


