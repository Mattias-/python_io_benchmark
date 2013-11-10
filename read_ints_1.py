
import sys

num_lines, k = map(int, sys.stdin.readline().split())
count = 0
lines = sys.stdin.readlines()
for line in lines:
    if int(line) % k == 0:
        count += 1
print count
