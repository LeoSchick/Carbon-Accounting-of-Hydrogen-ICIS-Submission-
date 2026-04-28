import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests as req



## Defintion of the Elektrolyzer as a class
from models.electrolyzer import Elektrolyzer

## Get Access Token for Green Grid API 
def get_access_token():
    url = 'https://signin.energy/am/oauth2/realms/root/realms/difesp/access_token'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }   
    data = {
        'client_id': 'esp_LeoSchickHydroNETTeAlavfv_001',
        'client_secret': 'n4FfnjmWz23GUI5hQLzimPVY',
        'grant_type': 'client_credentials',
        'scope': 'esp'
    }

    response = req.post(url, headers=headers, data=data)
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        print("Access Token:", access_token)
        return access_token
    else:
        print(f"Error: {response.status_code}")
        return None 
    
### Define Access to Carbon Data from Green Grid Compass ###

def get_ping(access_token):
    url = 'https://explore.traxes.io/greengrid-compass/v1/ping'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = req.get(url, headers=headers)
    if response.status_code == 200: 
        data = response.json()
        return data 
    else:
        print(f"Error: {response.status_code}")
        return None 
    
access_token = get_access_token()
ping = get_ping(access_token)
print(ping)


def get_carbon_data(access_token):
    url = 'https://explore.traxes.io/greengrid-compass/v1/co2-intensity'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    parameters = {
        'start': '2026-04-20T00:00:00Z',
        'end': '2026-04-27T00:00:00Z',
        'zone': 'DE_LU',
        'time-resolution': 'Hourly',
        'calculation-type': 'Consumption',
        'emission-type': 'Operational'
    }
    response = req.get(url, headers=headers, params=parameters)
    if response.status_code == 200: 
        data = response.json()
        return data 
    else:
        print(f"Error: {response.status_code}")
        return None 
    
access_token = get_access_token()
carbon_data = get_carbon_data(access_token)
print(carbon_data)