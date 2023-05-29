skaitli = []
ievade = int(input("Ievadiet skaitli: "))

while ievade != 0:
    if ievade % 2 == 0:
        skaitli.append(ievade)
    ievade = int(input("Ievadiet skaitli: "))

if len(skaitli) > 0:
    videjais = sum(skaitli) / len(skaitli)
    print("Pāru skaitļu vidējais aritmētiskais:", videjais)
else:
    print("Nav ievadīti pāra skaitļi.")