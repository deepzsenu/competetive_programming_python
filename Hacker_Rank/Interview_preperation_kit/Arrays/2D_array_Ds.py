#2darray
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    n = float("-inf")
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            total = sum(arr[i][j:j+3])+ arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            
            if total> n:
                n = total
    return n
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
