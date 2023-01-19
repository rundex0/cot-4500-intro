import numpy
a = numpy.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(a)

a[a == 0] = 3
print("\n",a)

a = numpy.delete(a, 2, 1)
print("\n",a)
