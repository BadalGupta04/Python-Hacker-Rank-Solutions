# Enter your code here. Read input from STDIN. Print output to STDOUT

x = range(int(input()))
for i in x:
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except BaseException as err:
        print("Error Code:", err)
