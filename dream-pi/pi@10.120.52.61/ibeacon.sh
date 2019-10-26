hciconfig hci0 up
hciconfig hci0 leadv 3
hciconfig hci0 noscan
hcitool -i hci0 cmd 0x08 0x0008 17 02 01 06 03 03 aa fe 0f 16 aa fe 10 00 02 77 65 62 67 61 7a 65 72 08 00 00 00 00 00 00 00 00