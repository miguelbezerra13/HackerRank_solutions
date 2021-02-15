#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    allowed_range = list(range(1,101))
    
    if (n and all(ar)) in allowed_range:
        sock_dict = {}
        for sock in ar:
            if sock not in sock_dict.keys():
                sock_dict[sock] = 1
            else:
                sock_dict[sock] += 1
        
        n_pairs = 0
        for count in sock_dict.values():
            n_pairs += int(count/2)
            
        return n_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
