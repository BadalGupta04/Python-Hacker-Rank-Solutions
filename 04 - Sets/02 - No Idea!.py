# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
l = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0

for i in l:
    if i in a:
       happiness += 1
    elif i in b:
        happiness -= 1

print(happiness)
