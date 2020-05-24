# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import scrapy
from scrape_train_information.items import ScrapeTrainInformationItem

filename = 'train_consist.txt'

class TrainSpiderSpider(scrapy.Spider):
    name = 'train_spider'
    allowed_domains = ['www.trainman.in/coach-position/']
    
    def start_requests(self):
        train_numbers = [16381, 16382, 11041, 11042]
        
        urls = ['http://www.trainman.in/coach-position/' + str(train_num) for train_num in train_numbers]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        output =  response.xpath('//*[@id="wrapper-content"]/main/coach-position-details/div/div/div/div/div/div//text()').extract()
        number = response.url.split('/')[-1]
        print(number)
        print(output)
        if 'ICF' in output[-2]:
            rakeType = 'ICF'
        elif 'LHB' in output[-2]:
            rakeType = 'LHB'
        else:
            raise Exception('Rake Type should either be ICF or LHB')
        
        
        coach_list = output[-1].split('--')
        ab_count = len([coach for coach in coach_list if coach.find('AB') == 0])
        ha_count = len([coach for coach in coach_list if coach.find('HA') == 0])
        threeTierAC = len([coach for coach in coach_list if coach.find('B') == 0]) + ab_count
        twoTierAC = len([coach for coach in coach_list if coach.find('A') == 0])
        firstAC = len([coach for coach in coach_list if coach.find('H') == 0]) +  ha_count
        sleeper = len([coach for coach in coach_list if coach.find('S') == 0])
        pantryIndicator = len([coach for coach in coach_list if coach.find('PC') == 0])
        
        data_row = []
        data_row.append(datetime.date.strftime(datetime.date.today(), '%d/%m/%Y'))
        data_row.append(datetime.date.strftime(datetime.date.today(), '%d/%m/%Y'))
        
        data_row.append(number)
        data_row.append(threeTierAC)
        data_row.append(twoTierAC)
        data_row.append(firstAC)
        data_row.append(sleeper)
        data_row.append(pantryIndicator)
        data_row.append(rakeType)
        
        data_row.append('origin')
        data_row.append('destination')
        
        train_consists = pd.read_csv("C:\\DataScience\\Github\\PythonOOP\\train_consists.csv")
        train_consists.loc[len(train_consists)] = data_row
        train_consists.to_csv("C:\\DataScience\\Github\\PythonOOP\\train_consists.csv", index=False)
        
        
