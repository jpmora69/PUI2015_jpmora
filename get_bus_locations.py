# coding: utf-8
import json
import sys
import csv
import urllib2
name1 = sys.argv[1]
name2 = sys.argv[2]
name3 = sys.argv[3]
url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + name1 + '&VehicleMonitoringDetailLevel=calls&LineRef=' + name2
request = urllib2.urlopen(url)
data = json.loads(request.read())
buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)
        for s in buses:        
            if s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'].startswith(' ') and s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'].startswith(' '):
                buslat= s['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
                buslon = s['MonitoredVehicleJourney']['VehicleLocation']['Longitude'] 
                stopstatus= 'N/A'
                stopname = 'N/A'
                print '%s, %s, %s, %s' % (buslat, buslon, stopname, stopstatus)        
                writer.writerow([buslat, buslon, stopname, stopstatus])
            else:
                buslat= s['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
                buslon = s['MonitoredVehicleJourney']['VehicleLocation']['Longitude'] 
                stopstatus= s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
                stopname = s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                print '%s, %s, %s, %s' % (buslat, buslon, stopname, stopstatus)        
                writer.writerow([buslat, buslon, stopname, stopstatus])
                
