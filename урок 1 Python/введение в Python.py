#x1= int(input('number 1: '))
#x2= int(input('number 2: '))
#def summa(a,b):
#    z=a+b
#    print(z)
#    return(z)
#summa(x1,x2)


a = int(input('number 1: '))
b = int(input('number 2: '))

def SquareNumber (num1,num2):
    if num1*num2==num1:
        return f'{num1} yes {num2}'
    elif num1*num1==num2:
        return f'{num2}yes{num1}'
    else:
        return 'no'
print(SquareNumber())

