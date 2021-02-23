#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    
    n = len(arr)
    
    if (n > 0) and (n <= 100) and (all(arr) >= -100) and (all(arr) <= 100):
        
        prop_pos, prop_neg, prop_zero = 0, 0, 0
        
        just_pos = [num for num in arr if num > 0]
        just_neg = [num for num in arr if num < 0]
        just_zero = [num  for num in arr if num == 0]
        
        prop_pos = round(len(just_pos)/n, 6)
        prop_neg = round(len(just_neg)/n, 6)
        prop_zero = round(len(just_zero)/n, 6)
        
    print(prop_pos)
    print(prop_neg)
    print(prop_zero)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)
    
