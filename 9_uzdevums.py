skaitli = []

while True:
    ievade = int(input("Ievadiet skaitli, lai pabeigtu darbību ievadiet 0): "))
    if ievade == 0:
        break
    if ievade % 2 == 0:
        skaitli.append(ievade)

if skaitli:
    videjais = sum(skaitli) / len(skaitli)
    print("Pāru skaitļu vidējais aritmētiskais:", videjais)
else:
    print("Nav ievadīti pāra skaitļi.")
