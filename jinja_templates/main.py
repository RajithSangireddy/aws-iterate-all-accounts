accounts = list({"1111111111","22222222222"})
sso_url = "https://yoursso.awsapps.com/start"
sso_role_name = "Devops"
sso_region = "us-east-1"
region= "us-east-1"

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('config.j2')
output_from_parsed_template = template.render(accounts=accounts,sso_url=sso_url,sso_role_name=sso_role_name,sso_region=sso_region,region=region)
print(output_from_parsed_template)

# to save the results
with open("config", "w") as fh:
    fh.write(output_from_parsed_template)