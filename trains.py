# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:29:53 2020

Railway booking system

Goal:
    1. Make bookings and lock a seat
    2. Modify bookins
    
@author: cgokh
"""

class Train:
    
    def __init__(self, number, coaches, ac3, ac2, ac1, sl, coach_type,
                 destination, origin):
        
        self._number = number
        self._coaches = coaches
        self._ac3 = ac3
        self._ac2 = ac2
        self._ac1 = ac1
        self._sl = sl
        self._coach_type = coach_type
        self._destination = destination
        self._origin = origin
        
        # All trains have 2 slr coaches
        self._slr = 2
        
        # Class invariants
        if not isinstance(self._number, int):
            raise ValueError(f"Expected an int, got a {type(self._number)} instead")
            
        
    def get_details(self):
        
        print(f"This number of this train is {self._number} going from \
              {self._origin} to {self._destination}")
                                 
    def create_consist(self):
        '''
        Steps:
            1. Create coach numbers
            2. Create a dict having seats in each coach as values and coach no. as key
            3. Create a dict for each seat and initialize the values with Nones and keys as seat details
            4. Return the object
        '''
        self._ac3_coach_list = ['B'+i for i in [str(i) for i in range(1, self._ac3 + 1)]]
        self._ac2_coach_list = ['A'+i for i in [str(i) for i in range(1, self._ac2 + 1)]]
        self._ac1_coach_list = ['H'+i for i in [str(i) for i in range(1, self._ac1 + 1)]]
        self._sl_coach_list = ['S'+i for i in [str(i) for i in range(1, self._sl + 1)]]
        self._all_coach_list = self._ac3_coach_list + self._ac2_coach_list + self._ac1_coach_list + self._sl_coach_list
        
        self._seating = {key:dict() for key in self._all_coach_list}
        
        for coach, seats in self._seating.items():
            print("This ran")
            if coach.find('S') == 0:
                print("This ran 2")
                self._seating[coach] = {seat:[] for seat in [str(i) for i in range(1, 81)]} 
            elif coach.find('B') == 0:
                print("This ran 3")
                self._seating[coach] = {seat:[] for seat in [str(i) for i in range(1, 73)]}
            elif coach.find('A') == 0:
                self._seating[coach] = {seat:[] for seat in [str(i) for i in range(1, 55)]}
            elif coach.find('H') == 0:
                self._seating[coach] = {seat:[] for seat in [str(i) for i in range(1, 23)]}
        
    
    def get_consist(self):
        if hasattr(self, '_seating'):
            return(self._seating)
        else:
            print("Consist hasn't been created yet")