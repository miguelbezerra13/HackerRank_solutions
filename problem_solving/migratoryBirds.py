#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):

    if (5 <= arr_count <= 2*pow(10, 5)) and (all(arr) in list(range(1,6))):
        
        my_set = sorted(set(arr))
        keys, counter = [], []
        
        for num in my_set:
            keys.append(num)
            counter.append(arr.count(num))
        
        return keys[counter.index(max(counter))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()