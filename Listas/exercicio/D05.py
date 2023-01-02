valores = list()
pares = list()
impar = list()
while True:
    valores.append(int(input("Digite um valor: ")))
    r = str(input("Quer continar? [s/n] "))
    if r in "Nn":
        break
for i,v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print("==" * 30)
print(f"A lsita completa e {valores}")
print(f"A lista de pares {pares}")
print(f"A lista de impares {impar}")
