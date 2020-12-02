#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    maxi = float('-inf')
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        #check the indices!!
    temp = 0
    for i in range(1, (len(arr)-1)):
        for j in range(1, (len(arr[0])-1)):
            temp += arr[i-1][j-1]
            temp += arr[i-1][j]
            temp += arr[i-1][j+1]
            temp += arr[i][j]
            temp += arr[i+1][j-1]
            temp += arr[i+1][j]
            temp += arr[i+1][j+1]
            if temp > maxi:
                maxi = temp
            temp = 0
    print(maxi)
