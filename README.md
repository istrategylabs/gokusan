# S3 Deploy

## Usage

First, create a s3Deploy.yml file in the root of the repository you want to deploy. Add your provided AWS credentials to it...

```
s3_bucket: '...'
s3_access_key: '...'
s3_secret_key: '...'
cloudfront_distribution_id: '...' # (optional)
```

1. Run `s3Deploy build` to run a 'sample' build to make sure everything works correctly.
1. Run `s3Deploy deploy` to deploy your site to S3.
1. Run `s3Deploy open` to open your deployed site in a browser window.
