n = int(input())
s = set(map(int, input().split()))

x = int(input())
for i in range(x):
    choice=input().split()
    if choice[0]=="pop" :
        s.pop()
    elif choice[0]=="remove":
        s.remove(int(choice[1]))
    elif choice[0]=="discard":
        s.discard(int(choice[1]))
        
print(sum(s))
