#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

    if (1 <= n <= 1000) and (0 <= all(scores) <= pow(10,8)):
        
        min_val, max_val, break_max, break_min = scores[0], scores[0], 0, 0
        
        for score in scores[0:]:
            
            if score < min_val:
                min_val = score
                break_min += 1
                
            elif score > max_val:
                max_val = score
                break_max += 1
                
        return break_max, break_min

n = 6
scores = [0, 9, 3, 10, 2, 20]
breakingRecords(scores)