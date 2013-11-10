
import sys

num_lines, k = map(int, sys.stdin.readline().split())
print len([x for x in sys.stdin if int(x) % k == 0])
