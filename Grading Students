#!/bin/python3

import math
import os
import random
import re
import sys 


def gradingStudents(grades):
    list=[]
    for i in range(len(grades)):
        if grades[i]>=38:
            value=grades[i]%5;
            minus=5-value
            if minus<=2:
                list.append(grades[i]+minus)
            else:
                list.append(grades[i])    
        else:
            list.append(grades[i])
    return list

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
