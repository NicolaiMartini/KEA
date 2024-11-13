from random import choice # Til øvelse 3.1.5

# 3.1.1 - opret en liste med 4 items og tilføj efterfølgende en ekstra item med .append() metoden
fruits=["apple","banana","cherry","orange"]
fruits.append("pineapple")
print(fruits)

# 3.1.2 - print item på index 0 fra listen
print(fruits[0])

# 3.1.3 - udskift det item på index 3 i listen med en ny item
fruits[3]="coconut"
print(fruits)

# 3.1.4 - lav en liste med 6 items hvor 3 af dem er ens
duplicates=1,2,2,2,3,4,5
print(duplicates)

# 3.1.5 - Print et random tal fra en liste For at gøre dette skal man lave en liste med integers ved at skrive: terning = [1, 2, 3, 4, 5, 6]
# Man kan importere choice funktionen fra random modulet og bruge choice(terning) for at få returneret et random item fra listen.
# Prøv at printe en string der simulere to terningkast ved at vælge et random item fra listen terning to gange og printe restultatet.
terning = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x=int(input("Vælg hvor mange gange D20-terningen skal kastes: "))
for i in range(x):
    print(choice(terning))