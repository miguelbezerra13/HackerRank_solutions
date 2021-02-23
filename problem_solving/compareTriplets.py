#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    
    al, bob = 0, 0
    
    if (all(a) >= 1) and (all(a) <= 100) and (all(b) >= 1) and (all(b) <= 100):
        
        for elem in range(3):
            
            if a[elem] > b[elem]:
                al += 1
            
            elif a[elem] < b[elem]:
                bob += 1
            
    return al, bob
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()