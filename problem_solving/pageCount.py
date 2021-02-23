#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    
    if 1 <= p <= n <= pow(10, 5):
        
        # Define if you are supposed to start from the beginning or the end
        
        # If the difference between the target page and the beginning is larger than the last page
        # and the target one, you should start from the end
        if p - 1 > n - p:
            start_at_1 = False
        
        # If the target page is the one in the middle
        elif p - 1 == n - p:
            
            # Start from the end if the target page is even and the last page is odd
            if p%2 == 0 and n%2 != 0:
                start_at_1 = False
            
            # Start from the beginning otherwise
            else:
                start_at_1 = True
        
        # If the difference between the target page and the beginning is smaller than the difference
        # between the last page and the targer one, start from the beginning
        else:
            start_at_1 = True
        
        # =============================================================================
        # Starting from the beginning
        # =============================================================================
    
        if start_at_1:
            # In case the target page is the first 1, you do not have to do anything
            if p == 1:
                count = 0
            
            # In case it is any other page
            else:
                # If the target page is even, you take the integer of half the difference of the
                # target page and the first one and then you add one
                if p%2 == 0:
                    count = int((p-1)/2)+1
                
                # Else, you do the same but do not add 1
                else:
                    count = int((p-1)/2)
                    
        # If you should start from the end
        else:
            # If the book has an even number of pages, the last page will be on the left
            if n%2 == 0:
                left, right = n, None
            
            # If the page has an odd number of pages, the last page will be on the right and you
            # should also consider the page on the left, as it might be the target page
            else:
                left, right = n-1, n
            
            # If the target page is the last or the one before in case the book has an odd number
            # of pages, you do not have to do anything
            if p == left or p == right:
                count = 0
            
            # In case it isn't
            else:
                # If the book has an even number of pages and the target page is uneven, you should
                # take the integer of half the difference between the last and the target pages and
                # then add one
                if n%2 == 0 and p%2 != 0:
                    count = int((n-p)/2)+1
                
                # Else you don't add 1
                else:
                    count = int((n-p)/2)
                    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
