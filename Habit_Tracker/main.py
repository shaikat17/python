import requests
from datetime import datetime
import os


USERNAME = os.getenv('Pixe_User_name')
TOKEN = os.getenv('Pixe_Token')
#TODAY = ''.join(str(date.today()).split('-'))

TODAY = datetime.utcnow()

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes"
}

#..................Create User...................

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
	"id": "graph1",
	"name": "Coding",
	"unit": "Done",
	"type": "int",
	"color": "shibafu"
}

headers = {
	"X-USER-TOKEN": TOKEN
}

#....................Create Graph..................

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_config = {
	"date": TODAY.strftime("%Y%m%d"),
	"quantity": "10"
}

#.......................Create Pixel...............

#response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
#print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{TODAY.strftime('%Y%m%d')}"

update_pixel_config = {
	"quantity": "6"
}


#........................Update Pixel...................
#response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
#print(response.text)
