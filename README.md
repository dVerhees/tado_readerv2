# tado_readerv2
Python Tado script for sending data to Domoticz

Credits: rjblake, chrism0dwk, http://blog.scphillips.com
Combined their information/modified their scripts to form this.

Functions:

- Read internal temperature and humidity
- Read current boiler power request percentage
- Read outside temperature
- Read solar strength in percentages
- Allows secure connection to Domoticz

Configure all information in tado_reader.py

User crontab or similar to execute this python script every x minutes
Tado limit is once every minute.

DISCLAIMER: Script might break as Tado is constantly changing their API at the
moment. I will update this as long as I'm still using it and find issues.
