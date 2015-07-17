# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
N = int(raw_input())

print ([[x, y, z] for x in range(0, x+1) for y in range(0, y+1) for z in range(0, z+1) if x + y + z != N])
