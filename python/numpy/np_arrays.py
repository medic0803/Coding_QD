import numpy

def arrays(arr):
    return numpy.flip(numpy.array(arr, dtype='f'))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
