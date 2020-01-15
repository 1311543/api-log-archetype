.PHONY:
.ONESHELL:
aws:
	read -p "* Set your Acess Key: " access_key
	aws configure set aws_access_key_id $$access_key
	read -p "* Set your Secret Key: " secret_key
	aws configure set aws_secret_access_key $$secret_key

aws-list:
	read -p "* Set a S3 bucket to test : " bucket
	aws s3 ls s3://$$bucket --recursive --human-readable --summarize