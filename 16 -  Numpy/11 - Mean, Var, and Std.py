import numpy 

n, m = map(int, input().split())
arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
np_arr = numpy.array(arr)
print(numpy.mean(np_arr, axis=1))
print(numpy.var(np_arr, axis=0))
print(numpy.round(numpy.std(np_arr, axis=None), decimals=11))