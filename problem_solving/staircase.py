#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    
    if (n > 0) and (n <= 100):
        
        num_hastags = 1
        num_spaces = n-1
        
        for num in range(n):
            hastags = '#'*num_hastags
            spaces = ' '*num_spaces
            print(spaces+hastags)
            num_hastags+=1
            num_spaces-=1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
