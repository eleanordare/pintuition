# -*- coding: utf-8 -*-

import datetime
from highcharts import Highchart
from pinterest import PinterestMethods

H = Highchart()

H.set_options('chart', {'type': 'spline'})

H.set_options('xAxis', {'type': 'datetime',
            'minRange': 14 * 24 * 3600000,
            'dateTimeLabelFormats': {'month': '%e. %b', 'year': '%b'},
            'title': {'text': 'Date'}})

H.set_options('yAxis',{'title': { 'text': 'Pins added'}})

H.set_options('title', {'text': 'Number of Wedding Pins'})

H.set_options('legend', {'enabled': False})


pinterestMethods = PinterestMethods()
pins = pinterestMethods.getBoardPins()
fullPinData = pinterestMethods.getPinsPerDay(pins)
data = fullPinData

H.add_data_set(data, 'line', 'Date Posted', pointInterval=24 * 3600 * 1000,
	pointStart=datetime.datetime(2006,1,1))
H.set_options('plotOptions', {
            'spline': {
                'marker': {
                    'enabled': True
                }
            }
        })

H.save_file()
