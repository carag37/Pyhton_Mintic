import random
    
def principal():
    numero_elegido = int(input("Elige un número del 1 al 10: "))
    numero_aleatorio = random.randint(1,10)
    while numero_aleatorio != numero_elegido:
        if numero_elegido > 10 or numero_elegido < 0:
            print("número inválido")
        else:
            if (numero_aleatorio > numero_elegido):
                print("elige un número mayor")
            else:
                print("buscar un número más pequeño")
        numero_elegido = int(input("Elige un número del 1 al 10: "))
    print("¡Ganaste!")
    print(numero_elegido)

if __name__=='__main__':
    principal()
