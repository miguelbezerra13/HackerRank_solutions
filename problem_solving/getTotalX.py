#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    
    length = [len(a), len(b)]
    arrs = [a, b]
    
    if (1 <= all(length) <=10) and (1 <= all(arrs) <= 100):
        
        counter = 0
        
        for num in range(max(a), min(b)+1):
            
            cond_1, cond_2 = True, True
            
            for ele_a in a:
                
                if num%ele_a != 0:
                    cond_1 = False
            
            for ele_b in b:
                
                if ele_b%num != 0:
                    cond_2 = False
            
            if cond_1 and cond_2:
                counter += 1
                
    return counter
                    

a = [2, 4]
b = [16, 32, 96]
total = getTotalX(a, b)
print(total)