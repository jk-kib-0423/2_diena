import random

min = 1
max = 20
skaitlis = random.randint(min, max)
meginajumi = 0

print(f"Dators mēģinās uzminēt skaitli intervālā no {min} līdz {max}.")

while True:
    minejums = random.randint(min, max)
    meginajumi += 1
    
    print(f"Dators min: {minejums}")
    
    if minejums == skaitlis:
        print("Dators ir uzminējis skaitli!")
        print(f"Lai uzminētu, tam tas prasīja {meginajumi} mēģinājumus.")
        break