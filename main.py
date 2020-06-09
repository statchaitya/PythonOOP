# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:17:33 2020

@author: cgokh
"""

import os
import datetime
os.chdir('C:\\DataScience\\Github\\PythonOOP')

import trains


# Create a train instance using its number
dadar_chennai_express_12163 = trains.Train(12163)


# Create a One Way Journey for today's date
journey_date = datetime.date.today()
dadar_chennai_express_today = trains.OneWayDetail(dadar_chennai_express_12163,\
                                                  journey_date)

# Adding a passenger
# .. Creating passenger object
chaitanya_gokhale = PassengerDetails("Chaitanya Gokhale", 28, "M")
# .. Adding passenger to the desired seat
dadar_chennai_express_today.add_passenger('B1', '1', chaitanya_gokhale)

dadar_chennai_express_today.booking_chart['B1']['1']
