#!/usr/bin/env python
__author__ = 'Eleanor Mehlenbacher'

import urllib, urllib2, json
from datetime import datetime, timedelta

access_token="AWRuspwOpmEWxbbkTD2gGNDnmt79FIzt04E4NzVDmoq4pAAu4AAAAAA"
pinterestUrl="https://api.pinterest.com/v1/"

boardUrl = "https://api.pinterest.com/v1/boards/eleanordare/wedding/pins?access_token=AWRuspwOpmEWxbbkTD2gGNDnmt79FIzt04E4NzVDmoq4pAAu4AAAAAA&fields=created_at&limit=100"

class PinterestMethods():

    pinWeeks = []

    # pull down JSON of instance info from Jenkins
    def getBoardPins(self):
        pinDates = []

        request = urllib2.Request(boardUrl)
        data = json.load(urllib2.urlopen(request))

        for i in data["data"]:
            pinDates.append(self.getDatesFromPin(i["created_at"]))

        while data["page"]["next"] is not None:
            request = urllib2.Request(data["page"]["next"])
            data = json.load(urllib2.urlopen(request))
            for j in data["data"]:
                pinDates.append(self.getDatesFromPin(j["created_at"]))

        return pinDates


    def getDatesFromPin(self, pin):
        pinDate = datetime.strptime(pin, '%Y-%m-%dT%H:%M:%S')
        pinWeek = datetime.strftime(pinDate, '%W')
        pinYear = datetime.strftime(pinDate, '%Y')
        self.pinWeeks.append(pinWeek + " " + pinYear)
        return pinDate.date()


    def getPinsPerWeek(self, pinWeeks):
        pinWeekCount = {}

        for x in pinWeeks:
            if not pinWeekCount.has_key(x):
                pinWeekCount[x] = 1
            else:
                pinWeekCount[x] = pinWeekCount[x] + 1

        return


    def getPinsPerDay(self, pinDates):
        pinDateCount = {}
        fullPinData = []

        for x in pinDates:
            if not pinDateCount.has_key(x):
                pinDateCount[x] = 1
            else:
                pinDateCount[x] = pinDateCount[x] + 1

        for y in pinDateCount.keys():
            if y.year == 2016:
                fullPinData.append([datetime.combine(y, datetime.min.time()), pinDateCount[y]])

        return sorted(fullPinData, key=lambda x: x[0], reverse=False)



if __name__ == '__main__':
    pinterestMethods = PinterestMethods()
    pins = pinterestMethods.getBoardPins()
    pinWeeks = pinterestMethods.pinWeeks
    pinWeekCount = pinterestMethods.getPinsPerWeek(pinWeeks)

    fullPinData = pinterestMethods.getPinsPerDay(pins)
    print fullPinData

    sortedPinWeeks = sorted(pinWeeks)
