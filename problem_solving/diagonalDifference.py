#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    good_to_go = True
    for line in range(len(arr)):
        if (all(arr[line]) < -100) and (all(arr[line]) > 100):
            good_to_go = False
            break
        break
    
    if good_to_go == True:
        diag_1, diag_2 = 0, -1
        sum_diag_1, sum_diag_2 = 0, 0
        
        for line in range(len(arr)):
            sum_diag_1 += arr[line][diag_1]
            sum_diag_2 += arr[line][diag_2]
            diag_1+=1
            diag_2-=1
            
    return abs(sum_diag_1-sum_diag_2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
