https://github.com/benkehoe/aws-sso-util
export AWS_DEFAULT_SSO_START_URL= <value>
export AWS_DEFAULT_SSO_REGION= <value>
aws-sso-util configure populate --region <region-name>

## run the below script to login to each account
for p in $(aws configure list-profiles | grep <keyword>); do echo $p && export AWS_PROFILE=$p && <script.sh/script.py>; done
