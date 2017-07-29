import base64
import urllib2


from interface.py import Tado

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

# Getvalues
outsideTemp = t.getOutsideTemp()
power = t.getPower(1)
climate = t.getClimate(1)

if debug: 
    print outsideTemp
    print power
    print climate
    
#if debug:
#    print "Retrieved HVAC info:"
#    print json.dumps(json_climate, indent=4)
    
tadoinsideTemp = climate['temperature']
tadohumidity = climate['humidity']    
tadoOutsideTemp = outsideTemp['outsideTemperature']
tadoSunPower = outsideTemp['solarIntensity']
tadoBoilerPower = power['power']

if debug: 
    print tadoinsideTemp
    print tadohumidity

domoticzurlinttemp = ("http://" + domoticzURL + "/json.htm?type=command&param=udevice&idx=" + domoticzIDXinttemp + "&nvalue=0&svalue=" + str(tadoinsideTemp) + ";" + str(tadohumidity) + ";0")
base64string = base64.encodestring('%s:%s' % (domoticzusername, domoticzpassword)).replace('\n', '')

if debug:
    print "Complete URL for submission to Domoticz"
    print domoticzurlinttemp
    
request1 = urllib2.Request(domoticzurlinttemp)
request1.add_header("Authorization", "Basic %s" % base64string)
res = urllib2.urlopen(request1)    
    
if debug: 
    print tadoOutsideTemp
    print tadoSunPower

domoticzurltemp = ("http://" + domoticzURL + "/json.htm?type=command&param=udevice&idx=" + domoticzIDXtemp + "&nvalue=0&svalue=" + str(tadoOutsideTemp) + ";0")
base64string = base64.encodestring('%s:%s' % (domoticzusername, domoticzpassword)).replace('\n', '')

if debug:
    print "Complete URL for submission to Domoticz"
    print domoticzurltemp

request2 = urllib2.Request(domoticzurltemp)
request2.add_header("Authorization", "Basic %s" % base64string)
res = urllib2.urlopen(request2)

domoticzurlsun = ("http://" + domoticzURL + "/json.htm?type=command&param=udevice&idx=" + domoticzIDXsun + "&nvalue=0&svalue=" + str(tadoSunPower) + ";0")
base64string = base64.encodestring('%s:%s' % (domoticzusername, domoticzpassword)).replace('\n', '')

if debug:
    print "Complete URL for submission to Domoticz"
    print domoticzurlsun

request3 = urllib2.Request(domoticzurlsun)
request3.add_header("Authorization", "Basic %s" % base64string)
res = urllib2.urlopen(request3)

if debug: 
    print tadoBoilerPower

domoticzurlbpow = ("http://" + domoticzURL + "/json.htm?type=command&param=udevice&idx=" + domoticzIDXbpow + "&nvalue=0&svalue=" + str(tadoBoilerPower) + ";0")
base64string = base64.encodestring('%s:%s' % (domoticzusername, domoticzpassword)).replace('\n', '')

if debug:
    print "Complete URL for submission to Domoticz"
    print domoticzurlbpow

request4 = urllib2.Request(domoticzurlbpow)
request4.add_header("Authorization", "Basic %s" % base64string)
res = urllib2.urlopen(request4)
