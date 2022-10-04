#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    currentLevel=0
    NumberOfValley=0
    for steps in path:
        if steps=="D":
            currentLevel-=1
            if currentLevel==-1:
                NumberOfValley+=1
        elif steps=="U":
            currentLevel+=1
    return NumberOfValley
        
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
