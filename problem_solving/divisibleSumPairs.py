#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):

    if (2 <= n <= 100) and (1 <= k <= 100) and (1 <= all(ar) <= 100):
        
        counter = 0
        for idx_s in range(len(ar)-1):
            
            num_s = ar[idx_s]
            
            for num_b in ar[idx_s+1:]:
                
                if (num_s+num_b)%k == 0:
        
                    counter += 1
                    
        return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
