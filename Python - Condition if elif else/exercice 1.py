a = int(input("Quelle est la mesure de la première longueur de votre triangle?>  "))
b = int(input("Quelle est la mesure de la deuxième longueur de votre triangle?>  "))
c = int(input("Quelle est la mesure de la troisième longueur de votre triangle?>  "))

if a == b == c:
    print("Votre triangle est équilatéral")
elif a == c != b:
    print("Votre triangle est isocèle")
else:
    print("Votre triangle n'est ni équilatéral ni isocèle")


