pessoas = list()
galera = list()
maior = menor = 0
while True:
    pessoas.append(str(input("Nome: ")))
    pessoas.append(int(input("Peso: ")))
    if len(galera) == 0:
        menor = maior = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    r = str(input("Quer Continuar? [S/N] "))
    if r in "Nn":
        break
print(f"Você cadastrou {len(galera)} pessoas ")
print(f"O maior peso {maior}kg foi de ", end="")
for p in galera:
    if p[1] == maior:
        print(f"{p[0]}")
print(f"O menor peso {menor}kg foi de ", end="")
for p in galera:
    if p[1] == menor:
         print(f"{p[0]}")
        