import sys
from requests.auth import HTTPBasicAuth
import os, requests
from termcolor import (colored)

SAUCE_USERNAME = os.environ["SAUCE_USERNAME"]
SAUCE_ACCESS_KEY = os.environ["SAUCE_ACCESS_KEY"]

#First arg in command is sc_tunnel_data.py

#seconf arg is the username
user = sys.argv[1]

#Third arg is the user's access key
# user_key = sys.argv[2]

#fourth arg is the tunnel ID
tunnel_id = sys.argv[2]


dataCenter = ['us-west-1', 'eu-central-1', 'us-east-1', 'apac-southeast-1']
region = 0

response = requests.get("https://api."+ dataCenter[region] +".saucelabs.com/rest/v1/" + user +"/tunnels/" + tunnel_id + "" , auth=HTTPBasicAuth(SAUCE_USERNAME, SAUCE_ACCESS_KEY))

if int(response.status_code) != 200:
	print(response.status_code)
	print(dataCenter[region])
	region =+ 1
	print(dataCenter[region])

	response = requests.get("https://api."+ dataCenter[region] +".saucelabs.com/rest/v1/" + user +"/tunnels/" + tunnel_id + "" , auth=HTTPBasicAuth(SAUCE_USERNAME, SAUCE_ACCESS_KEY))


print (colored("Release: ", 'green'), response.json()['metadata']['release'])
print (colored("Command: ", 'green'), response.json()['metadata']['command'])

if str(response.json()['status']) == 'running':
	print(colored("Status: ", 'green'), colored(response.json()['status'], 'green', attrs=['blink', 'underline']))
else:
	print(colored("Status: ", 'green'), colored(response.json()['status'], 'red'))
	print(colored("User Shut Down: ", 'green'), colored(response.json()['user_shutdown'], 'red'))


if str(response.json()['tunnel_identifier']) != '':
	print (colored("Tunnel Identifier: ", 'green'), response.json()['tunnel_identifier'])
else:
	print (colored("Tunnel Identifier: ", 'green'), colored("none", 'red'))

if str(response.json()['shared_tunnel']) == 'true':
	print (colored("Shared Tunnel: ", 'green'), response.json()['shared_tunnel'])
else:
	print (colored("Shared Tunnel: ", 'green'), colored(response.json()['shared_tunnel'], 'red'))

print (colored("Command Arguments: ", 'green'), response.json()['metadata']['command_args'])
