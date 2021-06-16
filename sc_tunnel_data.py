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
# user = 'TheTeejers'

try:
	tunnelResponse = requests.get('https://api.us-west-1.saucelabs.com/rest/v1/' + user + '/tunnels', auth=HTTPBasicAuth(SAUCE_USERNAME, SAUCE_ACCESS_KEY))

	tunnelList = tunnelResponse.json()

	print(tunnelResponse.status_code)
	print(len(tunnelResponse.json()))
	if tunnelResponse.status_code != 200:
		print(colored('No username ' + user + ' in our records.  Please check capitalization and spelling.', 'red'))
		quit(1)

#if more than one running tunnel, a list is provided

	elif len(tunnelList) > 0:
		print("yo")
		for x in tunnelList:
			index = tunnelList.index(x)
			print( index + 1, ')   ' + x)
	#if the tunnel ID is in the list, input y or n
		while True:
			tunnelIsRunning = input(colored("Do you see the tunnel ID in question listed above? (Y/N)\n", "green"))
		#if y or n not inputted
			if tunnelIsRunning.capitalize() != 'Y' and tunnelIsRunning.capitalize() != 'N' :
				print(colored("Please select either Y or N\n", "red"))
			else:
				break

	#if y is input
		if tunnelIsRunning.capitalize() == "Y":
	#if the tunnel was in the list, select the number in the list
			while True:
				tunnelNumber = input(colored("What number is the tunnel in the list?\n", "green"))
				if int(tunnelNumber) > len(tunnelList):
					print(colored('Please pick a number in the list above', 'red'))
				else:
					break
			for n in tunnelList:
				selected = tunnelList.index(n) +1
				if int(tunnelNumber) == int(selected):
					tunnel_id = n

	#if n is input
		elif tunnelIsRunning.capitalize() == "N":
				tunnel_id = input(colored("What's the tunnel ID?\n", "green"))

	else:
		print('No running tunnels')
		tunnel_id = input(colored("What's the tunnel ID?\n", "green"))
except:
	print(colored('There was an error', 'red'))
	quit(1)


# print(tunnel_id)

#Example Tunnel Owner Username:
# user = 'TheTeejers'


#enter Tunnel ID:
# tunnel_id = input(colored("What's the tunnel ID?\n", "green"))

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

try:
	print (colored("Command Arguments: ", 'green'), response.json()['metadata']['command_args'])
except:
	print(" ")
