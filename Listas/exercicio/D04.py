valores = list()
while True:
    n = int(input("Digite um valor: "))
    valores.append(n)
    r = str(input("Quer continar? [s/n] "))
    if r in "Nn":
        break
print("==" * 30)
print(f"você digitou {len(valores)} elementos")
valores.sort(reverse=True)
print(f"valores em ordem decresente {valores}")
if 5 in valores:
    print(f"O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")