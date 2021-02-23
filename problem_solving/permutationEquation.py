#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    
    if (1 <= len(p) <=50) and (1 <= all(p) <= 50):
        z = list(range(1, len(p)+1))
        order = []
        
        for x in range(1, len(p)+1):
            order.append(p.index(z[p.index(x)])+1)
        
    return order

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
