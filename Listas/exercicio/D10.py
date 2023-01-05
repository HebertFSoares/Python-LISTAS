matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = maior = scol = 0
for linha in range(0,3):
    for c in range(0,3):
        matriz[linha][c] = int(input(f"Digite um valor pra [{linha}, {c}]: "))
for linha in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[linha][c]:^5}]", end="")
        if matriz[linha][c] % 2 == 0:
            spar += matriz[linha][c]
    print()
print("-" * 30)
print(f"a soma dos valores pares é {spar}")
for l in range(0,3):
    scol += matriz[linha][2]
print(f"A soma dos valores da terceira coluna é {scol}")
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}")
