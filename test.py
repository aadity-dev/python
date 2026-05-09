# import boto3
# client = boto3.client('s3')
# #client - low level - more control, more complex
# # resource - high level - less control, easier to use
# response = client.list_buckets()
# print(response)



import boto3

# Create S3 client
client = boto3.client('s3')

# Bucket name must be globally unique
bucket_name = "adi-learning-bucket-12345"

# Create bucket
response = client.create_bucket(
    Bucket=bucket_name
)

print("Bucket created successfully!")
print(response)