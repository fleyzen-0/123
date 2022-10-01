number1 = int(input("Введіть два числа "))
number2 = int(input())
if number1%2!=0:
    number1 +=1
while number1 <= number2:
    print(number1)
    number1 += 2
