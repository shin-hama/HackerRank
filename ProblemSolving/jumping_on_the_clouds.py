#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    thunder = 1

    current = 0
    for i, _ in enumerate(c):
        try:
            if c[current+2] == 0:
                current += 2
            else:
                current += 1
        except IndexError:
            current += 1

        if current == len(c):
            break

    return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
