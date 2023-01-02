expr = str(input("Digite a Expressão: "))
pilha = list()
for simb in expr:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão está valida")
else:
    print("Sua expressão está errada")