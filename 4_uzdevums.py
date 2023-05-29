vērtējums = int(input("Lūdzu, ievadiet savu vērtējumu programmēšanā (no 1 līdz 10): "))

if vērtējums == 10:
    print("Izcili!")
elif vērtējums >= 8:
    print("Teicami!")
elif vērtējums >= 5:
    print("Viduvēji!")
else:
    print("Vāji!")