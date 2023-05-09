VET = []
posicoes_repetidas = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    VET.append(num)

for i in range(len(VET)):
    num = VET[i]
    if VET.count(num) > 1 and num not in posicoes_repetidas:
        posicoes_repetidas.append(i)

if len(posicoes_repetidas) > 0:
    print("Os seguintes números aparecem mais de uma vez no vetor:")
    for i in posicoes_repetidas:
        print(f"O número {VET[i]} se repete na posição {i+1}")
else:
    print("Não há números iguais no vetor.")