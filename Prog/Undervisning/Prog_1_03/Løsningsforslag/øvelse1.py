# Undervisningsgang 3 øvelser

# Øvelse 1
"""
1.1 - opret en liste med 4 items og tilføj efterfølgende
en ekstra item med .append() metoden​
"""
fruits = ["banana", "pear", "strawberry", "kiwi"]
fruits.append("apple")
print(f"øvelse 1.1 {fruits}")
"""
1.2 - print item på index 0 fra listen​
"""
print(f"øvelse 1.2 {fruits[0]}")

"""
1.3 - udskift det item på index 3 i listen med en ny item​
"""
fruits[3] = ["Durian"]
print(f"øvelse 1.3 {fruits}")

"""
1.4 - lav en liste med 6 items hvor 3 af dem er ens​
"""
komponenter = ["modstand", "kondensator", "LED", "Potmeter", "Potmeter", "Potmeter"]
print(f"Øvelse 1.4: {komponenter}")

"""
1.5 - Print et random tal fra en liste​

 For at gøre dette skal man lave en liste med integers ved at skrive: ​

 terning = [1, 2, 3, 4, 5, 6]​

Man kan importere choice funktionen fra random modulet og bruge​
choice(terning) for at få returneret et random item fra listen. Prøv at​
printe en string der simulere to terningkast ved at vælge et random​
item fra listen terning to gange og printe restultatet.
 """
from random import choice

terning = [1, 2, 3, 4, 5, 6]

print("Øvelse 1.5: Du har slået :", choice(terning),"og", choice(terning))