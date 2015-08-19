# Enter your code here. Read input from STDIN. Print output to STDOUT

string = raw_input().strip()
sub_string = raw_input().strip()

i=0

while string.find(sub_string) > -1:
   string = string[string.find(sub_string) + 1:]
   i += 1

print (i)
