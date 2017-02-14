import sys

a = []
answer_array = []
for line in sys.stdin:
    a.append(map(int, line.strip().split()))

for i in range(len(a)):
    