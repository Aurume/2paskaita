#  Leistų vartotojui po vieną įvesti 5 žodžius
#  Pridėtų įvestus žodžius į sąrašą
#  Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
#  Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį.


zodziai = []

for i in range(5):
    zodziai.append(input("Įveskite žodį: "))
for fraze in zodziai:
    print(fraze, len(fraze), zodziai.index(fraze))
