sudėti = 0

while True:
    sk = int(input("Įveskite norimą skaičių: "))
    if sk < 0:
        break
    sudėti += sk

print(sudėti)