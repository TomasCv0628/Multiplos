"""Programa que lea dos numeros enteros y averigues si el uno es multiplo del otro"""

print("\nꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤ")
print("ꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤ")
print("ꕤꕤꕤꕤꕤꕤꕤ NUMEROS MULTIPLOS ꕤꕤꕤꕤꕤꕤꕤ")
print("ꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤ")
print("ꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤꕤ\n")


X = int(input("\nIngrese el primer numero: "))
Y = int(input("\nIngrese el segundo numero: "))

if X >= Y:
    if X % Y == 0:
        print("\nEl segundo numero es multiplo del primero")
    else:
        print("\nLos numeros no son multiplos")
elif X <= Y:
    if Y % X == 0:
        print("\nEL primer numero es un multiplo del segundo")
    else:
        print("\nLos numeros no son multiplos")
else:
    print("\nLos numeros no son multiplos")