# Enter your code here. Read input from STDIN. Print output to STDOUT

M = raw_input()
a = raw_input()
l1 = a.split()
newl1 = list(map(int, l1))
set1 = set(newl1)

N = raw_input()
b = raw_input()
l2 = b.split()
newl2 = list(map(int, l2))
set2 = set(newl2)

x = set1.union(set2)
y = set1.intersection(set2)

for i in sorted(list(x - y)):
    print i
