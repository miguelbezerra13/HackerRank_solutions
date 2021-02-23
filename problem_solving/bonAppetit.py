#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

    if (2 <= n <= pow(10, 5)) and (0 <= k <= n) and (0 <= all(bill) <= pow(10, 4)) and \
       (0 <= b <= sum(bill)):
        
        right_bill = bill
        del right_bill[k]
        if b == sum(right_bill)/2:
            print('Bon Appetit')
            
        else:
            print(int(b-sum(right_bill)/2))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
