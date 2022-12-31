valores = list()
for cont in range(0,5):
    valores.append(int(input("Digite um valor: ")))

for c,valor in enumerate(valores):
    print(f"na posição {c} encontrei o valor {valor}!")
     
print("Final da Lista")