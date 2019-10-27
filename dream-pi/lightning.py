from time import sleep
import requests
from requests.auth import HTTPBasicAuth
import json

username = "admin"
password = "adminadmin123"

reserved_url = "https://dreambag.herokuapp.com/data/reserved"
hue_url = "http://10.120.51.245/api/pb6rOn7EdLcBkKGx2Ovo7u719Dzqx8DJ2gxVrOg7/lights/3/state"

red_h = 0
red_s = 254
red_v = 254

green_h = 25500
green_s = 254
green_v = 254

def make_red():
    r = requests.put(hue_url, json={
        "on": True,
        "bri": red_v,
        "hue": red_h,
        "sat": red_s,
    })

def make_green():
    r = requests.put(hue_url, json={
        "on": True,
        "bri": green_v,
        "hue": green_h,
        "sat": green_s,
    })

auth = HTTPBasicAuth(username, password)

#user "pb6rOn7EdLcBkKGx2Ovo7u719Dzqx8DJ2gxVrOg7"

#led_green = LED(20) # red
#led_red = LED(21) # green
red_on = False

while True:
    if red_on:
        make_red()
    else:
        make_green()
    sleep(0.3)

    

    r = requests.get(reserved_url, auth=auth)
    json_status = r.json()
    try:
        content = json_status["data"]["reserved"]
    except:
        content = False
    


    # 0 means it's not reserved
    if bool(content) is True:
        red_on = True
    else:
        red_on = False
        
