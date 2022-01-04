lista = []
with open("input.txt", "r", encoding="utf8") as f:
    for szam in f:
        lista.append(int(szam))

print(f"1. Hány eleme van a sorozatnak? {len(lista)}")
negativ = False
for elem in lista:
    if elem < 0:
        print("2. Van-e a sorozatban negatív szám? Van")
        negativ = True
        break
if negativ == False:
    print("2. Van-e a sorozatban negatív szám? Nincs")
db = 0
max = lista[0]
for elem in lista:
    if elem%2==0:
        db+=1
    if max < elem:
        max = elem
print(f"3. Hány páros szám található a sorozatban? {db}")
print(f"4. Mennyi a sorozatban található legnagyobb szám? {max}")
print("5. Írjuk ki a sorozatban található 10-zel osztható számokat!")
for elem in lista:
    if elem%10==0:
        print(elem)        