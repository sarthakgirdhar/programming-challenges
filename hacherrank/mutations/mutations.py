# Enter your code here. Read input from STDIN. Print output to STDOUT

S = raw_input()
i, c = raw_input().split()

string = S[:int(i)] + c + S[int(i)+1:]
print string
