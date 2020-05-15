# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:29:53 2020

Railway booking system

Goal:
    1. Create a train run using train and seating details
        - create train and seating details
    2. Modify bookins
    
@author: cgokh
"""

import pandas as pd
import os

class Train:
    
    def __init__(self, number):
        ''' 
        
        Initializes the rake details from a csv file sitting on disk (or server)
        
        Rake details are not fixed and rakes keep changing and hence
        
        '''
        # Using this number we will init the corresponding train
        self._number = number
        self._consist_created = False
        
        # Download rake info
        train_consists = pd.read_csv(os.path.join("C:\\DataScience\\Github\\PythonOOP", "train_consists.csv"))
        # Filter rake info for specific train
        train_consists = train_consists[train_consists['Number'] == number]
        train_consists.DateModified = pd.to_datetime(train_consists.DateModified)
        latest_modified_date = train_consists.DateModified.min()
        current_consist = train_consists[train_consists['DateModified'] == latest_modified_date]
        
        # Checking if current_consist has only 1 row
        if not current_consist.shape[0] == 1:
            raise ValueError(f"There should only be one latest consist")
            
        # Fetch rake info and init
        self._threeTierAC = int(current_consist["ThreeTierAC"])
        self._twoTierAC = int(current_consist["TwoTierAC"])
        self._firstAC = int(current_consist["FirstAC"])
        self._sleeper = int(current_consist["Sleeper"])
        self._pantry = int(current_consist["PantryIndicator"])
        self._rakeType = current_consist["RakeType"]
        self._destination = current_consist["Destination"]
        self._origin = current_consist["Origin"]
        
        # All trains have 2 slr coaches. SLR stands for seating-cum luggage rake
        self._SLR = 2
        
        # Class invariants
        if not isinstance(self._number, int):
            raise ValueError(f"Expected an int, got a {type(self._number)} instead")
            
    
    def num_coaches(self):
        ''' Returns total number of coaches '''
        
        return self._threeTierAC + self._twoTierAC + self._firstAC + self._sleeper + self._pantry + self._SLR
    
    def get_details(self):
        ''' Prints train details '''
        
        print(f"This number of this train is {self._number} going from \
              {self._origin} to {self._destination}")
                                 
    def create_consist(self):
        '''
        Creates consist of a train based on the current alignment of coaches
        '''
        if not self._consist_created:
            self._threeTierAc_coachList = ['B'+i for i in [str(i) for i in range(1, self._threeTierAC + 1)]]
            self._twoTierAC_coachList = ['A'+i for i in [str(i) for i in range(1, self._twoTierAC + 1)]]
            self._firstAC_coachList = ['H'+i for i in [str(i) for i in range(1, self._firstAC + 1)]]
            self._sleeper_coachList = ['S'+i for i in [str(i) for i in range(1, self._sleeper + 1)]]
            self._all_coachList = self._threeTierAc_coachList + self._twoTierAC_coachList + self._firstAC_coachList + self._sleeper_coachList
            
            self._seating = {key:dict() for key in self._all_coachList}
            
            for coach, seats in self._seating.items():
                if coach.find('S') == 0:
                    self._seating[coach] = {seat:[] for seat in [str(i) for i in range(1, 81)]} 
                elif coach.find('B') == 0:
                    self._seating[coach] = {seat:[] for seat in [str(i) for i in range(1, 73)]}
                elif coach.find('A') == 0:
                    self._seating[coach] = {seat:[] for seat in [str(i) for i in range(1, 55)]}
                elif coach.find('H') == 0:
                    self._seating[coach] = {seat:[] for seat in [str(i) for i in range(1, 23)]}
            
        self._consist_created = True
        print("Success")
        
    def get_consist(self):
        if hasattr(self, '_seating'):
            return(self._seating)
        else:
            print("Consist hasn't been created yet")
            



# Testing


    
    
    
    