import numpy

n = numpy.array(list(map(float, input().split())), float)
x = float(input())
print(numpy.polyval(n, x))

