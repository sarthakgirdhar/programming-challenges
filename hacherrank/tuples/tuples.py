# Enter your code here. Read input from STDIN. Print output to STDOUT

from __builtin__ import hash

N = int(raw_input())
T = tuple(map(int, raw_input().strip().split(" ")))

print hash(T)
