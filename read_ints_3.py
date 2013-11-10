
import sys

num_lines, k = map(int, sys.stdin.readline().split())
count = 0
for line in sys.stdin:
    if int(line) % k == 0:
        count += 1
print count
