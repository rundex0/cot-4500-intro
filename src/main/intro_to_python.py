import numpy
a = numpy.matrix([[1, 3, 3], [3, 1, 3], [3, 3, 1]])
print(a)

a = numpy.matrix([[1, 3, 3], [3, 1, 3], [3, 3, 1]])
print("\n",a)

a = numpy.delete(a, 2, 1)
print("\n",a)
