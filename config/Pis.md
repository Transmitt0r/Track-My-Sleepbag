Pi 1:
    ip: 10.120.52.61
    hostname: sweetdreams1
    string: 0x08 0x0008 17 02 01 06 03 03 aa fe 0f 16 aa fe 10 5f 03 74 72 61 75 2e 6d 65 2f 31 00 00 00 00 00 00 00 00
    url: https://trau.me/1

Pi 2:
    ip: 10.120.52.74
    hostname: sweetdreams2
    string: 0x08 0x0008 17 02 01 06 03 03 aa fe 0f 16 aa fe 10 5f 03 74 72 61 75 2e 6d 65 2f 32 00 00 00 00 00 00 00 00
    url: https://trau.me/2

Pi 3:
    ip: 10.120.51.186
    hostname: sweetdreams3
    string: 0x08 0x0008 17 02 01 06 03 03 aa fe 0f 16 aa fe 10 5f 03 74 72 61 75 2e 6d 65 2f 33 00 00 00 00 00 00 00 00
    url: https://trau.me/3
Pi 4:
    ip: 10.120.52.96
    hostname: sweetdreams4

user: pi
pw: sweetdreams


sudo raspi-config -> change hostname

scp eddystone.sh pi@hostname:/home/pi
sudo chmod +x /home/pi/eddystone.sh

-> change variables

scp eddystone.service pi@hostname:/home/pi
sudo cp eddystone.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/eddystone.service

sudo systemctl daemon-reload
sudo systemctl enable eddystone.service

## On pi 4
scp lightning.service pi@hostname:/home/pi
sudo su -
cp lightning.service /lib/systemd/system/
chmod 644 /lib/systemd/system/lightning.service

systemctl daemon-reload
systemctl enable lightning.service
reboot

sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 3
sudo hcitool -i hci0 cmd $EDDY_URL