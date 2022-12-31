valores = list()
maior = 0
menor = 0
for cont in range(0,5):
    valores.append(int(input(f"Digite um valor para posição {cont}: ")))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(valores)
print(f"O Maior Valor Digitado {maior} na posição ", end="")
for i, v in enumerate(valores):
    if valores[i] == maior:
        print(f"{i}...", end="")
print()
print(f"O menor Valor Digitado {menor} na posição ",end="")
for i,v in enumerate(valores):
    if valores[i] == menor:
        print(f"{i}...")
print()