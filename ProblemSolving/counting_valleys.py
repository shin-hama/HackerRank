#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
SEA_LEVEL = 0


def countingValleys(steps, path):
    # Write your code here

    step_map = {'U': 1, 'D': -1}
    current = SEA_LEVEL

    result = 0
    for p in path:
        current += step_map[p]
        if current == SEA_LEVEL and p == 'U':
            result += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
