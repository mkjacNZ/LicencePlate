import requests
import os
import json
import urllib.request
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    # Photo by Kelvin Valerio from Pexels: https://www.pexels.com/photo/black-hyundai-suv-1519192/
    with open('testImages/car1.jpg', 'rb') as fp:
        
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            files=dict(upload=fp),
            headers={'Authorization': 'Token ' + os.getenv('TOKEN')})

    print("Licence plate number is: " + str(response.json()['results'][0]['plate']).upper())
    print("Vehicle type is: " + str(response.json()['results'][0]['vehicle']['type']))
    print("Licence plate region is: " + str(response.json()['results'][0]['region']['code']).upper())