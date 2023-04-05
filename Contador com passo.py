from time import sleep

def linha():
    print("-=" * 20 + "-")

#def primeiro(a, b, c):
#    while a <= b:
#        print(f"{a} ", end='')
#        a += c
#    print("FIM!")

def primeiro(a, b, c):
    for i in range(a,b):
        print(f"{a} ", end='', flush=True)
        sleep(0.5)
        a += c
    print("FIM!")

def segundo(a, b, c):
    while a >= b:
        print(f"{a} ", end='', flush=True)
        sleep(0.5)
        a -= c
    print("FIM!")

def terceiro(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        while a <= b:
            print(f"{a} ", end='', flush=True)
            sleep(0.5)
            a += c
    else:
        while a >= b:
            print(f"{a} ", end='', flush=True)
            sleep(0.5)
            a -= c
    print("FIM!")

#Contar de 1 ate 10 de 1 em 1
linha()
print("Contagem de 1 até 10 de 1 em 1")
primeiro(1, 10, 1)
linha()

#Contar de 10 ate 0 de 2 em 2
print("Contagem de 10 até 0 de 2 em 2")
segundo(10, 0, 2)
linha()

#Contagem personalizada
print("Agora é sua vez de personalizar a contagem!")
a = int(input("Início: "))
b = int(input("Fim:    "))
c = int(input("Passo:    "))
linha()
print(f"Contagem de {a} até {b} de {c} em {c}")
terceiro(a, b, c)