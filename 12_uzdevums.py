def minesana(skaitlis):
    min = 1
    max = 100
    minejums = (min + max) // 2

    while minejums != skaitlis:
        print("Dators min:", minejums)

        if minejums < skaitlis:
            min = minejums + 1
        else:
            max = minejums - 1

        minejums = (min + max) // 2

    print("Dators uzminēja! Skaitlis ir", minejums)