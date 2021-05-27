number1 = eval(input("enter number1: "))
number2 = eval(input("enter number2: "))
x= input ("enter *product or +sum or -sub or \div:")

if x == '/':
    print(number1/number2)
elif x == '*':
    print(number1*number2)
elif x == '+':
    print(number1+number2)
elif x == '-':
    print(number1-number2)
