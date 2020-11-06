#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    counter = defaultdict(int)
    for i in ar:
        counter[i] += 1

    result = 0
    for num in counter.values():
        result += num // 2

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()
