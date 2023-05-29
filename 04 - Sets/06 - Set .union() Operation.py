# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
seta = set(map(int, input().split()))
b = int(input())
setb = set(map(int, input().split()))

final = seta.union(setb)
print(len(final))

