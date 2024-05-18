import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    # another flip a list arr[::-1] <- uses a negative step parameter and empty start and stop
    floatArray = list(map(float, arr))
    numpyArray = numpy.array(floatArray)
    return numpy.flip(numpyArray)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)