# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=int(input('no of people: '))
m=[]
for i in range(n):
    m.append([False]*n)
for i in range(n):
    people=input(f'Enter listof people known to {i}: ').split()
    for p in people:
        p=int(p)
        m[i][p]=True
   
celebrity=None
for i in range(n):
    c=0
    for j in range(n):
        if m[i][j] is False:
            c=c+1    
    if c==n:
        for k in range(n):
            if m[k][i] is True:
                celebrity=i
            else:
                if k==i:
                    celebrity=i

if celebrity==None:
    print('no cele')
else:
    print(f'{celebrity} is cele')