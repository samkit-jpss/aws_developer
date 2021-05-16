import boto3

s3=boto3.resource("s3")  #Used s3 resource

bucket_name="bucketforme11"  #name of the bucket 
bucket_creation = s3.create_bucket(Bucket=bucket_name,
      CreateBucketConfiguration={
          'LocationConstraint': 'ap-south-1'})
