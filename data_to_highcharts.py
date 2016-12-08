#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Eleanor Mehlenbacher'

import datetime
from highcharts import Highchart
from pinterest import PinterestMethods

class HighchartsMethods():

    def main(self):
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

        H.add_data_set(data, 'area', 'Date Posted', pointInterval=24 * 3600 * 1000,
        	pointStart=datetime.datetime(2006,1,1))
        H.set_options('plotOptions', {
                    'area': {
                        'fillColor': {
                            'linearGradient': { 'x1': 0, 'y1': 0, 'x2': 0, 'y2': 1},
                            'stops': [
                                [0, "Highcharts.getOptions().colors[0]"],
                                [1, "Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')"]
                            ]
                        },
                        'marker': {
                            'enabled': True,
                            'radius': 3
                        },
                        'lineWidth': 1,
                        'states': {
                            'hover': {
                                'lineWidth': 1
                            }
                        }
                    }
                })

        H.save_file()
