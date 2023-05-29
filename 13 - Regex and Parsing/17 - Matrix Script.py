#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

traversed = [matrix[j][i] for i in range(m) for j in range(n)]
pattern = r'([a-z0-9])([^a-z0-9]+)([a-z0-9])'
decoded = re.sub(pattern, r'\1 \3', str.join('', traversed), 0, re.I) 
print(decoded)
