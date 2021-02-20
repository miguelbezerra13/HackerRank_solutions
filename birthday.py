#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):

    if (1 <= len(s) <= 100) and (1<= all(s) <=5) and (1 <= d <= 31) and (1 <= m <= 12):
        
        counter = 0
        for square in range(len(s)-m+1):
            
            if sum(s[square:square+m]) == d:
                
                counter += 1
                
        return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
