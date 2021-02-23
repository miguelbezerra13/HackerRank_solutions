#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    length = list(range(2,101))
    vals = [0, 1]
    
    if len(c) in length and all(c) in vals and c[0] == c[len(c)-1] == 0:
        
        min_jump = 1
        
        cloud_num = 0
        while cloud_num <= len(c):
            
            if cloud_num < len(c)-1:
                
                cloud_num += 2
                
                if cloud_num >= len(c)-1:
                    break
                
                if c[cloud_num] == 0:
                    pass
                else:
                    cloud_num -= 1
                min_jump += 1
            
        return min_jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
