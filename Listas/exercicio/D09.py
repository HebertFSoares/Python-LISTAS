matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for c in range(0,3):
        matriz[linha][c] = int(input(f"Digite um valor pra [{linha}, {c}]: "))
for linha in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[linha][c]:^5}]", end="")
    print()