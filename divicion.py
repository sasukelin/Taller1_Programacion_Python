dividendo = int(input("Ingrese un primer número: "))
divisor = int(input("Ingrese un segundo número: "))

resultado = float(dividendo) / float(divisor)
residuo = dividendo % divisor

print("El resultado de la división es:", resultado)

if residuo == 0:
    print("La división es exacta.")
else:
    print("La división no es exacta.")

