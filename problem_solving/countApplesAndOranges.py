#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    parameters = [s, t, a, b, len(apples), len(oranges)]
    max_dst = pow(10, 5)
    
    if ((all(parameters) >= 1) and (all(parameters) <= max_dst)) and \
       ((all(apples) >= -max_dst) and (all(apples) <= max_dst)) and \
       ((all(oranges) >= -max_dst) and (all(oranges) <= max_dst)) and \
       (a < s < t < b):
        
        fall_apples = [a+apple for apple in apples]
        fall_oranges = [b+orange for orange in oranges]
        
        house_apple = [apple for apple in fall_apples if (apple>=s and apple<=t)]
        house_orange = [orange for orange in fall_oranges if (orange>=s and orange<=t)]
    
        print(len(house_apple))
        print(len(house_orange))
            
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
