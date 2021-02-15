#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    if len(s) in list(range(1,101)) and n>=1 and n<=math.pow(10,12):
    
        a_to_check = 0
        
        if s == 'a':
            a_to_check = n
    
        else:
            num_as = 0
            for let in s:
                if let == 'a':
                    num_as += 1
            
            mega_str_len = n//len(s)
            a_to_check = num_as*mega_str_len
            
            dig_left = n%len(s)
            
            for let in s[:dig_left]:
                if let == 'a':
                    a_to_check += 1

    return a_to_check

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
