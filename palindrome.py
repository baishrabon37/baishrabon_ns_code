
# -*- coding: utf-8 -*-
"""
checking a string is pallindrome or not
@author: Baishrabon Karar
"""

s=input()
j=len(s)-1
i=0
flag=0
while(i<j):
    if(s[i]!=s[j]):
        flag=1
        break
    else:
        i+=1
        j-=1
if(flag==0):
    print("pallindrome")
else:
    print("not pallindrome") 
