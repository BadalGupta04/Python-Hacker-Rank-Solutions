# Enter your code here. Read input from STDIN. Print output to STDOUT


from collections import namedtuple


n, Student = int(input()), namedtuple('Student', input())
print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for i in range(n)]) / n))
