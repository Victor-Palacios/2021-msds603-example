eb init week2 --region us-west-2 --platform Docker --key $PEM_NAME
eb create week2-env --verbose --envvars AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --envvars AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY --envvars API_KEY=$API_KEY