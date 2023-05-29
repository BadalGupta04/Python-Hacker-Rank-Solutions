# Enter your code here. Read input from STDIN. Print output to STDOUT

from cmath import polar
z = complex(input())
print(*polar(z), sep='\n')
