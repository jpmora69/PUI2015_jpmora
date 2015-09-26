# coding: utf-8
import json
import sys
import urllib2
name1 = sys.argv[1]
name2 = sys.argv[2]
url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + name1 + '&VehicleMonitoringDetailLevel=calls&LineRef=' + name2
request = urllib2.urlopen(url)
data = json.loads(request.read())
buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print('Bus line: ') + str(sys.argv[2])
print('Number of monitored buses: ') + str(len(buses))
counter = -1
for s in buses:        
    buslat= s['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    buslon = s['MonitoredVehicleJourney']['VehicleLocation']['Longitude'] 
    counter +=1   
    print 'The bus %s is at latitude %s and longitude %s' % (counter, buslat,  buslon)
    
