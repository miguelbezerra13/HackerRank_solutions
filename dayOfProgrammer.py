#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    if 1700 <= year <= 2700:
        
        if year == 1918:
            date = '26.09.1918'
        
        else:
            
            if year >= 1919:
                if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
                    is_leap_year = True
                
                else:
                    is_leap_year = False
                
            elif year <= 1917:
                
                if year%4 == 0:
                    is_leap_year = True
                
                else:
                    is_leap_year = False
                    
            if is_leap_year:
                date = '12.09.'+str(year)

            else:
                date = '13.09.'+str(year)
            
        return date
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
