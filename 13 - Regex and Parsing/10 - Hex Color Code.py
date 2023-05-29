# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for i in range(int(input())): 
    match = re.findall(r"(\#[a-f0-9]{3,6})[\;\,\)]{1}", input(), re.I) 
    if match:
        for j in list(match):
            print(j)
