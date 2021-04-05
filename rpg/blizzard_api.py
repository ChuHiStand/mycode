#!/usr/bin/env python3


import requests
import json

client_id = "75f0c476dca443c289e3af7142127982"
client_secret = "M1HF37oIxwTA372L2bdNG1LOAF85dU85"

URL = "https://us.api.blizzard.com/data/wow/playable-class/index?namespace=static-us&locale=en_US&access_token=US8NrOVVatpwqi6R6hNsFjHE8ubbYu7hMM"
response = requests.get(URL).json()

# json_object = json.loads(response)
print(response["classes"][0]["name"])
