import json
with open('social.json') as json_file:  
	data = json.load(json_file)

print(data)