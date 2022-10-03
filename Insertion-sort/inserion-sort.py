#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
        j = n-1
        store = arr[j]
        
        for i in range(j, -1, -1):
            if store < arr[i-1] and i >= 1:
                arr[i] = arr[i-1]
                print(' '.join(str(x) for x in arr))
            else: 
                arr[i] = store
                print(' '.join(str(x) for x in arr))
                break 


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

