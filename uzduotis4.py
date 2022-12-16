# Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# Kitu atveju atspausdinti „Laimėjai!“

import random

print("3 skaičiai")
print("Jei vienas iš trijų yra 5, tu pralaimėjai!")

for x in range(3):
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Pralaimėjai")
        break
else:
    print("Laimėjai!")
