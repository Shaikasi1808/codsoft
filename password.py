from random import random
import math
n=int(input('enter length of the string'))
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
big=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','v','W','X','Y','Z']
sp=['-','@','!','#','$','?']
numbs=[0,1,2,3,4,5,6,7,8,9]
total=[small,big,sp,numbs]
password=""
for i in range(n):
    a=math.floor(random()*len(total))
    b=math.floor(random()*len(total[a]))
    st=total[a][b]
    st=str(st)
    password=password+st
print('your password is')
print(password)