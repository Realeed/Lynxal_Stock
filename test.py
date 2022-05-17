import requests
from bearer import getBearerToken

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "User-Agent": "python-requests/2.4.3 CPython/3.4.0",
    "X-DIGIKEY-Client-Id": "mEszZA7lW3tiCtvB8UAS4SlC8eDoGWPv",
    "Authorization": f"Bearer {getBearerToken()}",
}

mpn = f'311-0.0LRTR-ND'
r = requests.get(f'https://api.digikey.com/Search/v3/Products/{mpn}', headers = headers)
try:
    for i in range(len(r.json()["Parameters"])):
        if r.json()["Parameters"][i]["Parameter"] == "Power (Watts)":
            print("Power Rating is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Tolerance":
            print("Tolerance is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Features":
            print("Features are: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Package / Case":
            print("Package / Case is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Temperature Coefficient":
            print("Temperature Coefficient: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Size / Dimension":
            print("Size / Dimension is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Composition":
            print("Composition is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Operating Temperature":
            print("Operating Temperature is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Number of Terminations":
            print("Number of Terminations is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Supplier Device Package":
            print("Supplier Device Package is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Height - Seated (Max)":
            print("Height - Seated (Max): ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Failure Rate":
            print("Failure Rate is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Part Status":
            print("Part Status is: ", r.json()["Parameters"][i]["Value"])
        elif r.json()["Parameters"][i]["Parameter"] == "Resistance":
            print("Resistance is: ", r.json()["Parameters"][i]["Value"])
except:
    pass