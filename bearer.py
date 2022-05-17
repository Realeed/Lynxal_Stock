import requests
from openpyxl import load_workbook

path = "Excels\\bearer.xlsx"
wb = load_workbook(path)

sheet = wb.active

url = 'https://api.digikey.com/v1/oauth2/token'

headers = {
    "User-Agent": "python-requests/2.4.3 CPython/3.4.0",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {
    "client_id": "mEszZA7lW3tiCtvB8UAS4SlC8eDoGWPv",
    "client_secret": "u8N6QACwERbS83Y7",
    "refresh_token": sheet[2][0].value,
    "grant_type": "refresh_token"
}

def getBearerToken():
    r = requests.post(url=url, headers=headers, data=data)

    access_token = r.json()['access_token']
    refresh_token = r.json()['refresh_token']

    sheet[1][0].value = access_token
    sheet[2][0].value = refresh_token

    wb.save(path)

    return access_token
