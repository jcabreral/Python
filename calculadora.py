print("Bienvenido.")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("¿Qué desea hacer?")
print("1. Sumar \n2. Restar \n3. Multiplicar")

while(True):
    decision = int(input("Ingrese la operación a realizar: "))
    if decision == 1:
        suma = num1 + num2
        print("La suma de", num1, "y", num2,"es:", suma)
        break
    elif decision == 2:
        resta = num1 - num2
        print("La resta de", num1, "y", num2,"es:", resta)
        break
    elif decision == 3:
        mult = num1 * num2
        print("La multiplicación de", num1, "y", num2,"es:", mult)
        break
    else:
        print("Ingrese una opción valida")
        continue
