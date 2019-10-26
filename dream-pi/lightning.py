from gpiozero import LED
from time import sleep

import urllib2, base64


led_green = LED(20) # red
led_red = LED(21) # green
red_on = True

while True:
    if red_on:
        led_red.on()
        led_green.off()
    else:
        led_red.off()
        led_green.on()
    sleep(1)

    username =  ""
    password = ""

    request = urllib2.Request("https://dreambag.herokuapp.com/data/reserved")
    base64string = base64.b64encode('%s:%s' % (username, password))
    request.add_header("Authorization", "Basic %s" % base64string)   
    result = urllib2.urlopen(request)
    content = result.read()
    print(content)

    # 0 means it's not reserved
    if content is "0":
        red_on = False
    else:
        red_on = True
