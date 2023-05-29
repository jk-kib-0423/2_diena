for skaitlis in range(1, 101):
    if skaitlis % 3 == 0 and skaitlis % 5 == 0:
        print("BumRum")
    elif skaitlis % 3 == 0:
        print("Bum")
    elif skaitlis % 5 == 0:
        print("Rum")
    else:
        print(skaitlis)