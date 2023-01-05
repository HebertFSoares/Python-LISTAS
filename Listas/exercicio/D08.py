valores = list()
pares = list()
impar = list()
for cont in range(0,8):
    valores.append(int(input("Digite Valores: ")))
for i,v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
pares.sort()
impar.sort()
print(f"valores pares {pares}")
print(f"valores impares {impar}")