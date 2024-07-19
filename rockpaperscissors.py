import math
from random import random
ties=0
us=0
cs=0
r=0
while(1):
    print("pick one\n1.rock\n2.paper\n3.scissors\n")
    n=int(input("enter your choice"))
    arr=["rock","paper","scissors"]
    uc=arr[n-1]
    cc=arr[math.floor(random()*3)]
    print("your choice::",uc)
    print("computer choice::",cc)
    if(uc==cc):
        print("it's a tiee")
        ties=ties+1
    elif(uc=="rock" and cc=="scissors"):
        print("user wins!!")
        us=us+1
    elif(uc=="scissors" and cc=="rock"):
        print("computer wins")
        cs=cs+1
    elif(uc=="scissors" and cc=="paper"):
        print("user wins!!")
        us=us+1
    elif(uc=="paper" and cc=="scissors"):
        print("computer wins")
        cs=cs+1
    elif(uc=="paper" and cc=="rock"):
        print("user wins!!")
        us=us+1
    else:
        print("computer wins")
        cs=cs+1
    r=r+1
    print("if you want to play one more round enter 1 otherwise enter 0")
    y=int(input("1/0\n"))
    if(y==0):
        break;
print("final scores after",r," rounds")
print("user's score is",us)
print("computer's score is",cs)
print("no of ties",ties)
if(us>cs):
    print("yupp!!!ultimately you won:)")
elif(us<cs):
    print("oops!!! computer won :(")
    print("well played!better luck next time")
else:
    print("wow!!well fought but that's a draw")

    
   
    