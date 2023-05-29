# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
arr = list(map(int, input().split()))
myset = set(arr)

x = sum(myset)*k
y = sum(arr)

print((x-y)//(k-1))
