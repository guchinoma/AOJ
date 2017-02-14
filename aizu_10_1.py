import sys

def plus(line):
    a, b = line.split()
    return a + b

array = []
for line in sys.stdin:
    array.append(int(line))

for i in range(len(array)):
    plus(array[i])
