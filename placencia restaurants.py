#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Fri May 20 14:57:03 2016

@author: Tony
"""

import csv

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Method using Class

class Resto(object):

    def __init__(self):
        self.csvfile = 'placencia_food.csv'
        self.day_dict = {
            'sunday': 'open_sun',
            'monday': 'open_mon',
            'tuesday': 'open_tue',
            'wednesday': 'open_wed',
            'thursday': 'open_thur',
            'friday': 'open_fri',
            'saturday': 'open_sat',
            }

    def which_day(self, day):
      """
      Info  : Just a function to present the output.
      """
      with open('placencia_food.csv', 'rt') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if row[day] == 'yes']
        x = ' '
        for row in rows:
            x = x + row['restaurant_name']+ ' ' + row['operating_hours']+'\n'+'\n'
        return x
          

      f.close()

# Initiating the Class
PV = Resto()

if __name__ == '__main__':
  while True:
    user_input = input("Find out what's open! Please enter a day of the week: ").lower()
    if user_input in PV.day_dict.keys():
        print(PV.which_day(PV.day_dict[user_input]))
      
    elif user_input == 'end'
        break
    
    else:
      print()  
      print("I know you're hungry, can you Please enter a valid day!")
      print()
      
