num  = [2,5,9,1]
num.append(7)
num[2] = 3
num.sort(reverse=True)
num.insert(2,0)
#num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print("Não achei o numeor 4")
print(num)
print(f"essa lista tem {len(num)} elementos")