#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    if (all(arr) >= 1) and (all(arr) <= math.pow(10,9)):
        
        sum_min = sum(arr) - max(arr)
        sum_max = sum(arr) - min(arr)
        
        print(str(sum_min)+' '+str(sum_max))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
