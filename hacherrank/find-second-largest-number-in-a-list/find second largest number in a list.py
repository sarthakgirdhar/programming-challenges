# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())

lis = list(map(int, raw_input().strip().split()))[:N]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)
