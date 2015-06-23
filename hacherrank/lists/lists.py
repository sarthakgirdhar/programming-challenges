# Enter your code here. Read input from STDIN. Print output to STDOUT

L = []

N = int(raw_input())

for c in range(N):
    com = raw_input().strip().split(" ")
    if com[0] == "append":
        L.append(int(com[1]))
    elif com[0] == "insert":
        L.insert(int(com[1]), int(com[2]))
    elif com[0] == "remove":
        L.remove(int(com[1]))
    elif com[0] == "pop":
        L.pop()
    elif com[0] == "index":
        L.index()
    elif com[0] == "count":
        L.count()
    elif com[0] == "sort":
        L.sort()
    elif com[0] == "reverse":
        L.reverse()
    elif com[0] == "print":
        print L
    
    
