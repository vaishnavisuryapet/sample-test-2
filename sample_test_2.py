# -*- coding: utf-8 -*-
"""sample test-2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DblOblYcmDSjxUR9Gg2EwriRzEnLo6J6
"""

harry=int(input())
ron=int(input())
hermoine=int(input())
if harry>ron and harry>hermoine:
    print("harry is max")
elif ron>hermoine:
    print("ron is max")
else:
    print("hermoine is max")

n=int(input())
sum=0
count=0
while n>0:
  rem=n%10
  n=n//10
  count+=1
  if count==1 or count==3 or count==10 or count==8:
    sum=sum+rem
print(sum)
if sum%3==0:
  print("code found")
else:
  print("not found")

