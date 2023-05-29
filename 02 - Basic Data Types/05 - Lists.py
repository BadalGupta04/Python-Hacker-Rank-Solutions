if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range (N):
        x=input().split()
        y=x[0]
        if y=="insert":
            l.insert(int(x[1]),int(x[2]))
        if y=="print":
            print(l)
        if y=="remove":
            l.remove(int(x[1]))
        if y=="append":
            l.append(int(x[1]))
        if y=="sort":
            l.sort()
        if y=="pop":
            l.pop()
        if y=="reverse":
            l.reverse()
