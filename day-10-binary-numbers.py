#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    numstring = str(bin(n))[2::]
    most = 0
    temp = 0
    for i in numstring:
        if i == "1":
            temp += 1
        elif i == "0":
            if temp > most:
                most = temp
            temp = 0
    if temp > most:
        most = temp
    print(most)
