valores = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in valores:
        valores.append(n)
        print("Valor adicionado com sucesso")
    else:
        print("Valor Duplicado")
    r = str(input("Quer continar? [s/n] "))
    if r in "Nn":
        break
print('==' * 30)
valores.sort()
print(f"Você digitou os valores {valores}")
