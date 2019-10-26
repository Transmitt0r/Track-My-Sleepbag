#!/bin/bash

hciconfig hci0 up
hciconfig hci0 leadv 3
hcitool -i hci0 cmd 0x08 0x0008 17 02 01 06 03 03 aa fe 0f 16 aa fe 10 00 03 74 72 61 75 2e 6d 65 2f 31 00 00 00 00 00 00 00 00