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
# -------------- START Configuration Section --------------------------------#
#Set login info Tado
t = Tado('<TADOUSERNAME>', '<TADOPASSWORD>')
#t.getClimate(1) # Get climate, zone 1.
#t.getPower(1) # Get climate, zone 1.

# Your Domoticz installation (usually localhost:8080, without http://)
domoticzURL = ""
# the username / password of your Domoticz installation (optional, if you
# enabled authentication
domoticzusername = ""
domoticzpassword = ""

# the IDX from the indoor Temp/Humid dummy device in Domoticz
domoticzIDXinttemp = ""
# the IDX from the outside Temp dummy device in Domoticz
domoticzIDXtemp = ""
# the IDX from the sunpower dummy device in Domoticz
domoticzIDXsun = ""
# the IDX from the boilerpower device in Domoticz
domoticzIDXbpow = ""

#Set to 1 for debugging
debug = 0
# -------------- END Configuration Section ----------------------------------#

User crontab or similar to execute this python script every x minutes
Tado limit is once every minute.

DISCLAIMER: Script might break as Tado is constantly changing their API at the
moment. I will update this as long as I'm still using it and find issues.