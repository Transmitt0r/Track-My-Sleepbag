from flask import Flask
from bluetooth.ble import BeaconService

app = Flask(__name__)
beacons = []

class Beacon(object):
    def __init__(self, data, address):
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address
    def __str__(self):
        ret = "Beacon: address:{ADDR} uuid:{UUID} major:{MAJOR}"\
                " minor:{MINOR} txpower:{POWER} rssi:{RSSI}"\
                .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                        MINOR=self._minor, POWER=self._power, RSSI=self._rssi)
        return ret

@app.route('/')
def hello_world():
    return_str = ''
    for beacon in beacons:
        return_str += str(beacon) + "\n"
    return return_str

if __name__ == '__main__':
    service = BeaconService()
    nearby_devices = service.scan(2)
    beacons = [Beacon(data, address) for address, data in list(nearby_devices.items())]

    app.run(host='0.0.0.0', port=5000)