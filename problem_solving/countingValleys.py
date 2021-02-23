#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    
    if (steps > 1 and steps <= math.pow(10,6)):# and all(path) in {'U', 'D'}:
        
        height = 0
        valleys = 0
        
        for step in range(len(path)):        
            
            if height == 0 and path[step] == 'D':
                valleys += 1
            
            if path[step] == 'U':
                height+=1
            else:
                height -= 1
            
        return valleys
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
