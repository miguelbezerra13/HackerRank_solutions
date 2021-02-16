#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    if 'AM' in s:
        
        if '12' == s[:2]:
            h = '00'
            return h+s[2:-2]
        
        else:
            return s[:-2]
    
    elif 'PM' in s:
        
        if '12' == s[:2]:
            return s[:-2]
        
        else:
            h = str(int(s[:2])+12)
            return h+s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
