from gpiozero import LED
from time import sleep

import urllib2, base64, json


led_green = LED(20) # red
led_red = LED(21) # green
red_on = False

while True:
    if red_on:
        led_red.on()
        led_green.off()
    else:
        led_red.off()
        led_green.on()
    sleep(1)

    password = ""

    request = urllib2.Request("https://dreambag.herokuapp.com/data/reserved")
    base64string = base64.b64encode('%s:%s' % (username, password))
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)
    content_json = result.read()
    try:
        json_status = json.loads(content_json)
        content = json_status["data"]["reserved"]
    except:
        content = False
    


    # 0 means it's not reserved
    if bool(content) is True:
        red_on = True
    else:
        red_on = False
        
