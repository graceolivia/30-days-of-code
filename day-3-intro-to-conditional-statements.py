#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N%2 == 1:
        print("Weird")
    elif (N <= 5) and (N >= 2):
        print("Not Weird")
    elif (N >= 6) and (N <= 20):
        print("Weird")
    else:
        print("Not Weird")
