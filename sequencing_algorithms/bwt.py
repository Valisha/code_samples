#!/usr/bin/env python3
from collections import deque
import sys 
string = input(sys.argv[0])
new_string = []
string_list = deque(string) # deque is sometimes preferred over list, because it is faster and you can do many more things that you generally cannot do with lists, I want to use the rotate function on this string thus, used deque instead of a normal list
n = len(string)
for i in range(n):
    new_string.append("".join(string_list))
    string_list.rotate(1)
new_string.sort()
bwt = [i[-1] for i in new_string]
indexes = [(n - m.index('$')-1) for m in new_string]
col0 = sorted(bwt)
#print('\n'.join(col0))
col1 = [bwt[i]+col0[i] for i in range(n)]
#print('\n'.join(col1))
# iterating starting with bwt again 
list1 = sorted(bwt)
for j in range(n-2):
    list1.sort()
    list1 = [bwt[i]+list1[i] for i in range(n)]
print("Below is BWT transform")
print('\n'.join(list1)+'\n')
list1 = [e for e in list1 if not '$' in e]
assert''.join(list1[0])==string[:-1]  
