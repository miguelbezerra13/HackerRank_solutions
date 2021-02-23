#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    
    # Constraints
    if (1 <= n <= 1000) and (1 <= m <= 1000) and (1 <= b <= pow(10, 6)):
        
        # If the sum of the cheapest keyboard and usb drive is higher than the budget
        if min(keyboards) + min(drives) > b:
            return -1
        
        # Remove the prices above the budget
        small_keyboards = [k for k in keyboards if k <= b]
        small_drives = [d for d in drives if d <= b]
        
        # If it is lower or equal to the budget, start by sorting the list in a descending order        
        small_keyboards.sort(reverse=True)
        small_drives.sort(reverse=True)
        
        # See which set of components has the most expensive piece in order to start looping with
        # that set. If the highest price is equal, the loop should be started according to the
        # larger number of elements
        if max(small_keyboards) > max(small_drives):
            largest = 'k'
        
        elif max(small_keyboards) < max(small_drives):
            largest = 'd'
            
        else:
            if len(small_keyboards) >= len(small_drives):
                largest = 'k'
            else:
                largest = 'd'
        
        max_val = 0
        if largest == 'k':
            for k in small_keyboards:
                for d in small_drives:
                    if k + d <= b:                
                        if k+d > max_val:
                            max_val = k+d
        
        else:
            for d in small_drives:
                for k in small_keyboards:                    
                    if k + d <= b:
                        if k+d > max_val:
                            if k+d > max_val:
                                max_val = k+d
                                
        return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
