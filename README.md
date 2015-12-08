# Gokusan

## Usage

First, create a gokusan.yml file in the root of the repository you want to deploy. Add your provided AWS credentials to it...

```
s3_bucket: '...'
s3_access_key: '...'
s3_secret_key: '...'
cloudfront_distribution_id: '...' # (optional)
```

1. Run `gokusan build` to run a 'sample' build to make sure everything works correctly.
1. Run `gokusan deploy` to deploy your site to S3.
1. Run `gokusan open` to open your deployed site in a browser window.
