# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = input()
result = re.findall(
    r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",s,)
if result:
    for i in result:
        print(i)
else:
    print(-1)
