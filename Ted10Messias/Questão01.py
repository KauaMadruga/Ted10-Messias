numeros = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("\nNúmeros em ordem inversa:")
for numero in reversed(numeros):
    print(numero)