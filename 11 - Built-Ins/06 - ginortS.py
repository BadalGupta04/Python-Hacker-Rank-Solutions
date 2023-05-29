# Enter your code here. Read input from STDIN. Print output to STDOUT

string = input().strip()
    
print(*sorted(string, key = lambda x: (-x.islower(), x.isdigit() - x.isupper(), x in '02468', x)), sep='')
