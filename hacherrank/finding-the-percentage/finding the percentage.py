# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())

record = dict()
lst1 = list()

for i in range(0, N):
    a = raw_input()
    lst1 = a.split()
    n = lst1[0]
    lst1.remove(lst1[0])
    newlst1 = list (map (float, lst1))  # Converting everything else in lst1 (the marks) to float.
    record[n] = newlst1
    
name = raw_input()
total = 0

if name in record:
    marks = record[name]
    sub = len(marks)
    for num in marks:
        total += num

avg = total / sub
print "%.2f" %avg
    
