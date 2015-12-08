# Gokusan

![goku](http://vignette3.wikia.nocookie.net/dragonballfanon/images/5/54/KidGoku.jpg)

## Installation

1. Grab the source
1. `cd` into the source and run `python setup.py install`

## Usage

First, create a gokusan.yml file in the root of the repository you want to deploy. Add your provided AWS credentials to it...

```
s3_bucket: '...'
s3_access_key: '...'
s3_secret_key: '...'
cloudfront_distribution_id: '...' # (optional)
```

1. Run `gokusan <build directory>` where "build directory" is the directory containing the built files to upload to s3

## Features

- Uploads static files to s3
- Configures s3 bucket as static website
- Reads credentials and bucket name from yaml file
- Configures bucket policy to allow public access
- Pass filename to upload as website

## ToDo

- Check if folder contains index.html
- Automatically create and associate cloudfront distribution
- Automatically create iAm credentials and policies
- Automate bucket creation
