# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = input().split()
a = set(map(int, x))
m = int(input())
y = input().split()
b = set(map(int, y))

ans1 = a.difference(b)
ans2 = b.difference(a)
ans = ans1.union(ans2)
for i in sorted(ans):
    print(i)
