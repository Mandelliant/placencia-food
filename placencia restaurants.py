# -*- coding: utf-8 -*-
"""
Created on Fri May 20 14:57:03 2016

@author: Tony
"""

import csv
with open() as csvfile: #CSV Path goes here
    reader = csv.DictReader(csvfile)
    

def main():
  x = input('What\'s open right now? ')
  print() 
  
  #Monday
  if (x == 'Monday') or (x == 'monday'):
    import csv

    with open(, 'rt') as f: #CSV path goes here
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['open_mon'] == 'yes']

    for row in rows:
        print(row['restaurant_name'], row['operating_hours'], '\n')
        
        f.close()
        
  
  #Tuesday
  elif(x == 'Tuesday') or (x == 'tuesday'):
    import csv

    with open(, 'rt') as f: #CSV path goes here
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['open_tue'] == 'yes']

    for row in rows:
        print(row['restaurant_name'], row['operating_hours'], '\n')
      
  #Wednesday  
  elif(x == 'Wednesday') or (x == 'wednesday'):
    import csv

    with open(, 'rt') as f: #CSV path goes here
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['open_wed'] == 'yes']

    for row in rows:
        print(row['restaurant_name'], row['operating_hours'], '\n')
        
  #Thursday      
  elif(x == 'Thursday') or (x == 'thursday'):
    import csv

    with open(, 'rt') as f: #CSV path goes here
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['open_thur'] == 'yes']

    for row in rows:
        print(row['restaurant_name'], row['operating_hours'], '\n')
        
  #Friday      
  elif(x == 'Friday') or (x == 'friday'):
    import csv

    with open(, 'rt') as f: #CSV path goes here
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['open_fri'] == 'yes']

    for row in rows:
        print(row['restaurant_name'], row['operating_hours'], '\n')
        
        
        
        
  #Saturday      
  elif(x == 'Saturday') or (x == 'saturday'):
    import csv

    with open(, 'rt') as f: #CSV path goes here
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['open_sat'] == 'yes']

    for row in rows:
        print(row['restaurant_name'], row['operating_hours'], '\n')
        
        
        
        
  #Sunday      
  elif(x == 'Sunday') or (x == 'sunday'):
    import csv

    with open(, 'rt') as f: #CSV path goes here
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['open_sun'] == 'yes']

    for row in rows:
        print(row['restaurant_name'], row['operating_hours'], '\n')
    
    
  else:
      print('Please try a different search term')


#Need to make this only print with the if elif clauses and not print if the else block displays    
  print()
  
  
  print('These restaurants are all open today!')



if __name__ == "__main__":
  
   while 1 ==1:
      main()


            
