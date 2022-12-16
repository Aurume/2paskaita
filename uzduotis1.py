#  Sukurti list ir dictionary, kur butu galima:
# prideti
# istrinti
# pakeisti

list = [2, 8888, 7, 222, 45545, 33333, "Labas", 664, 23, 44]

print(list[2])

list.append(323)  # prideda reiksme
print(list)

list.insert(7, "Diena")  # ideda reiksme ten kur nurodau pagal index nr
print(list)

list.remove(222)  # pasalina nurodyta
print(list)

list.clear()
print(list)

metai = {"Narsutis": 65, "Teisutis": 70, "Katrina": 16}

print(metai["Katrina"])

metai["Teklė"] = 99
print(metai)

del metai["Katrina"]
print(metai)

metai["Teisutis"] = 55
print(metai)
