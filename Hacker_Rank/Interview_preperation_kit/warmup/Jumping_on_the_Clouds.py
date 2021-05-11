#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    #write your code here
    jump = 0 
    steps = 0 
    
    while (steps < (len(c)-2)):
        if c[steps+2]!=1:
            steps +=2
            jump+=1
        else:
            steps +=1
            jump+=1
    if steps == (len(c)-2):
        jump+=1
        
    return jump
    
    

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
