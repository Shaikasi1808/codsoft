num1=int(input("enter first value"))
num2=int(input("enter first value"))
print("  opearations are\n1.addition\n2.subtraction\n3.multiplication\n4.division\n5.modulodivision\n6.exponential\n")
operator=int(input("enter your choice"))
def opearation(num1,num2,op):
    if(op==1):
        return num1+num2
    elif(op==2):
        return num1-num2
    elif(op==3):
        return num1*num2
    elif(op==4):
        return num1/num2
    elif(op==5):
        return num1%num2
    else:
        return num1**num2
print("after performing the opeartion with the desired opeartor on given two numbers ")
print(" result is ")
print(opearation(num1,num2,operator))