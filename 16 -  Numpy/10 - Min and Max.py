import numpy

n, m = map(int, input().split())
arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
np_ar = numpy.array(arr)
print(numpy.max(numpy.min(np_ar, axis=1)))

