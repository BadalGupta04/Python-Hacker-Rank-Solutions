#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

class OrderedCounter(Counter):
    pass
    

if __name__ == '__main__':
    letters = OrderedCounter(sorted(input())).most_common(3)
    [print(*letter) for letter in letters]
