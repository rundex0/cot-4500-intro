import numpy
matrix = numpy.array(([1, 0, 0], [0, 1, 0], [0, 0, 1]))
print(str(matrix).replace(' [', '').replace('[', '').replace(']', ''), "\n")

matrix[matrix < 1] = 3
print(str(matrix).replace(' [', '').replace('[', '').replace(']', ''), "\n")

matrix = numpy.delete(matrix, 0, 1)
print(str(matrix).replace(' [', '').replace('[', '').replace(']', ''), "\n")
