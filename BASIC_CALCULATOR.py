a=int(input('Enter First Number : '))
b=int(input('Enter Second Number : '))
print('BASIC CALCULATOR\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION');
choice=int(input('Enter a choice : '))
if choice==1:
    print("Result =",a+b)
elif choice==2:
    print('Result = ',a-b)
elif choice==3:
    print('Result = ',a*b)
elif(choice==4):
    print('Result = ',a/b)
else:
    print('Wrong Input')
