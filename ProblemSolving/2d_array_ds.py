
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    length = len(arr)
    hourglass_len = 3
    retry = length - hourglass_len + 1

    maximum = -9 * 7 - 1
    for i in range(0, retry):
        for j in range(0, retry):
            total = 0
            for k in range(0, hourglass_len):
                if k == 1:
                    total += arr[i + k][j+1]
                else:
                    total += sum(arr[i + k][j:j+hourglass_len])

            maximum = max((total, maximum))

    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
