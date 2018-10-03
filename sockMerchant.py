'''
from itertools import groupby
n = int(raw_input())
c = map(int, raw_input().split())

ans = 0
for val in [len(list(group)) for key, group in groupby(sorted(c))]:
    ans = ans + val/2
print ans

'''

#my solution
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    i = 0
    pair = 0
    while i < n - 1:
        if ar[i] == ar[i+1]:
            pair += 1
            i += 2
        else:
            i += 1
    return (pair)
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
