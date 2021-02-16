#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    
    if (grades_count >= 1) and (grades_count <= 60) and (all(grades) >= 0) and (all(grades) <= 100):
        
         final_grades = []
         
         for grade in grades:
             
             if (grade <= 37) or ((grade % 5) <= 2):
                 final_grades.append(grade)
            
             elif (grade % 5) >= 3:
                rounded_grade = grade + (5-grade%5)
                final_grades.append(rounded_grade)
        
    return final_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
