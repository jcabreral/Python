def imprimir_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if (numero % factor = 0):
            print(factor, end = " ")
            numero /= factor
        else:
            factor += 1
    return "Done"

na = input("Ingrese un número: ")
n = int(na)
imprimir_factores_primos(n)
