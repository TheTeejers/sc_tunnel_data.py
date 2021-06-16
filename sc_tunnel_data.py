import sys
from requests.auth import HTTPBasicAuth
import os, requests
from termcolor import (colored)
import json

SAUCE_USERNAME = os.environ["SAUCE_USERNAME"]
SAUCE_ACCESS_KEY = os.environ["SAUCE_ACCESS_KEY"]

#First arg in command is sc_tunnel_data.py

#Enter the Tunnel Owner Username
user = input(colored("What's the tunnel owner username?\n", "green"))

#Example Tunnel Owner Username:
# user = 'TheTeejers'


#enter Tunnel ID:
tunnel_id = input(colored("What's the tunnel ID?\n", "green"))

#example Tunnel ID:
# tunnel_id = 'eac4e069271a4c14b096665214f2624f'


dataCenter = ['eu-central-1', 'us-west-1']
# dataCenter = ['us-west-1', 'eu-central-1', 'us-east-1', 'apac-southeast-1']

region = 0

try:

	for DC in dataCenter:
		response = requests.get("https://api."+ dataCenter[region] +".saucelabs.com/rest/v1/" + user +"/tunnels/" + tunnel_id + "" , auth=HTTPBasicAuth(SAUCE_USERNAME, SAUCE_ACCESS_KEY))
		if response.status_code == 200:
			break
		else:
			region =+ 1

	print (colored("Release: ", 'green'), response.json()['metadata']['release'])
except:
	print(colored("No tunnel matches the username`/`tunnel ID combination in any datacenter.", "red", attrs=['underline']))
	quit(1)


print (colored("URL: ", 'green'), "https://api."+ dataCenter[region] +".saucelabs.com/rest/v1/" + user +"/tunnels/" + tunnel_id + "")


if str(response.json()['metadata']['command']) != '':
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

if 'command_args' in response.json()['metadata'] in response.json():
	print (colored("Command Arguments: ", 'green'), response.json()['metadata']['command_args'])
