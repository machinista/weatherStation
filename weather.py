#!/usr/bin/env python

import time
import urllib2
import json
from microdotphat import clear, scroll, HEIGHT, write_string, scroll_vertical, show

def main():

    key = 'cc8047a5-a693-417a-9721-c6213690acbb'
    ely = '324249'
    cambridge = '350731'
    #fcDataType = wxfcs or wxobs
    weatherType = {
    'NA': 'Huh?', '1': 'Sunny', '2': 'Cloudy', '3': 'Cloudy', '4': 'Huh?', '5': 'Misty', '6': 'Foggy', '7': 'Cloudy',
    '8':"O'cast", '9': 'L-Shwr', '10': 'L-Shwr', '11': 'Drizzl', '12': 'L-Rain', '13': 'H-Shwr', '14': 'H-Shwr',
    '15': 'H-Rain', '16': 'L-Sleet', '17': 'L-Sleet', '18': 'Sleet', '19': 'L-Hail', '20': 'L-Hail', '21': 'Hail!!',
    '22': 'L-Snow', '23': 'L-Snow', '24': 'L-Snow', '25': 'Snow', '26': 'Snow', '27': 'H-Snow', '28': 'Stormy',
    '29': 'Stormy', '30': 'Stormy'
	}
    
    while True:
        response = urllib2.urlopen('http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/' + ely + '?res=3hourly&key=' + key)
        fcData = response.read()
        fcDataStr = fcData.decode('utf-8')
        fcDataDict = json.loads(fcDataStr)
        dataDate = (fcDataDict['SiteRep']['DV']['dataDate'])
        fcDate = (fcDataDict['SiteRep']['DV']['Location']['Period'][1]['value'])
        fcTime = (fcDataDict['SiteRep']['DV']['Location']['Period'][1]['Rep'][3]['$'])
        fcTemp = (fcDataDict['SiteRep']['DV']['Location']['Period'][1]['Rep'][3]['T'])
        fcPp = (fcDataDict['SiteRep']['DV']['Location']['Period'][1]['Rep'][3]['Pp'])
        fcWeather = (fcDataDict['SiteRep']['DV']['Location']['Period'][1]['Rep'][3]['W'])
        
        print '\n'
        print '**** New Data ****'
        print 'Forecast Date = ' + fcDate
        print 'Forecast time = ' + fcTime
        print 'Temp DegC = ' + fcTemp
        print 'Rain % = '+ fcPp
        print 'Weather type = ' + fcWeather
        weather = weatherType[fcWeather]
        print weather
        
        msg = 'Forecast: 9AM tomorrow'
        #write_string(msg, offset_x = 7, kerning = False)      
        write_string(weather, offset_y = 0, kerning = False)
        write_string('T: ' + fcTemp, offset_y = 7, kerning = False)
        write_string('R% ' + fcPp, offset_y = 14, kerning = False)
   
        for updateInterval in range(900):
            show()
            time.sleep(4)       
            for pixelRow in range(7):
                scroll_vertical()
                show()
                time.sleep(0.03)
        clear()

if __name__ == '__main__':
    main()
