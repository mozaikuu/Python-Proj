#first i fuck around

#can do math
print(1000 + 25 *30)
#can multiply string unlike javascript
print("he" * 10)

#now i start calculator
num1= float(input("enter number"))   #float is a number with decimal point
op= input("operator ")
num2= float(input("enter number"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "x":
    print(num1 * num2)
elif op == "%":
    print(num1 / num2)
elif op == "/": 
    print(num1 / num2)
elif op == "**":
    print(num1 * num1)
elif op == "***":
    print(num1 * num1 * num1)
elif op == "//":
    print(num1 / num1)
elif op == "///":
    print(num1 / num1 / num1)
else:
    print("invalid operator")



