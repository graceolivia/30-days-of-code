#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    string = ""
    arr = list(map(int, input().rstrip().split()))
    rarr = arr[::-1]
    for i in rarr:
        string += str(i)
        string += ' '
    print(string)
