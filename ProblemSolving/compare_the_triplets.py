#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.


def compareTriplets(a, b):
    result = [0, 0]
    for i, j in zip(a, b):
        if i > j:
            result[0] += 1
        elif i < j:
            result[1] += 1
        else:
            continue

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
