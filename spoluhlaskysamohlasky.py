import random
samohlasky = "aeiouy"
spoluhlasky = "bcdfghjklmnpqrstvwxz"
dlzka_retazec = random.randrange(8, 17)
vysledok = ""
for i in range (dlzka_retazec):
    if i % 2 == 0:
        temp = random.randrange (0, len(spoluhlasky))
        vysledok = vysledok + spoluhlasky[temp]
    else:
        temp = random.randrange (0, len(samohlasky))
        vysledok = vysledok + samohlasky[temp]
print (vysledok)