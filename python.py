print("Ingresar el primer número: ")
num1 = int(input())

print("Ingresar el segundo número: ")
num2 = int(input())

print("Ingresar el tercer número: ")
num3 = int(input())

print("Ingresar el cuarto número: ")
num4 = int(input())

if num1 >= num2 and num2 >= num3 and num3 >= num4:
    print(num1, "-", num2, "-", num3, "-", num4)
elif num2 >= num1 and num1 >= num3 and num3 >= num4:
    print(num2, "-", num1, "-", num3, "-", num4)
elif num3 >= num1 and num1 >= num2 and num2 >= num4:
    print(num3, "-", num1, "-", num2, "-", num4)
elif num4 >= num1 and num1 >= num2 and num2 >= num3:
    print(num4, "-", num1, "-", num2, "-", num3)
elif num4 >= num3 and num3 >= num1 and num1 >= num2:
    print(num4, "-", num3, "-", num1, "-", num2)
elif num3 >= num2 and num2 >= num1 and num1 >= num4:
    print(num3, "-", num2, "-", num1, "-", num4)
elif num2 >= num3 and num3 >= num1 and num1 >= num4:
    print(num2, "-", num3, "-", num1, "-", num4)
else:
    print("¡Se ingresaron números iguales!")
