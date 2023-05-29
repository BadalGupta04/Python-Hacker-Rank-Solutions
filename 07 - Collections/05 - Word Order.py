# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

N = int(input())
list = []

for i in range(N):
    list.append(input().strip())

count = Counter(list)

print(len(count))
print(*count.values())
