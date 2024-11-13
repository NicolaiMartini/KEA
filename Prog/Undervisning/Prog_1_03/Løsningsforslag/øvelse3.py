# Undervisningsgang 3 øvelser

# Øvelse 3

"""
3.2 Opret en dictionary frugt_priser, der indeholder priserne
på forskellige frugter. Brug get-metoden til at hente prisen på en frugt,
der findes i dictionaryen, og en frugt, der ikke findes.​
"""

fruit_prices_dkk = {
    "apple" : 4,
    "banana" : 5,
    "water melon" : 20,
    }
print("Øvelse 3.2:", fruit_prices_dkk.get("water melon"))
print("Øvelse 3.2:", fruit_prices_dkk.get("cherry"))

"""
3.3 Opdater prisen på en frugt i frugt_priser dictionaryen.​
"""
fruit_prices_dkk["apple"] = 2
print("\nØvelse 3.3:", fruit_prices_dkk)
"""
3.4 Brug values-metoden til at få en liste over alle
værdierne i frugt_priser dictionaryen.​
"""
print("\nØvelse 3.4:", fruit_prices_dkk.values())
"""
3.5 Brug keys-metoden til at få en liste over alle
nøglerne i frugt_priser dictionaryen.​
"""
print("\nØvelse 3.5:", fruit_prices_dkk.keys())
"""
3.6 Opret en dictionary student_grades med nogle studenter og deres karakterer.
Brug get-metoden til at hente en students karakter,
opdater en students karakter,
og brug values og keys metoderne til at få alle karakterer
og alle studentnavne.​
"""
student_grades = {
    "Kevin" : 10,
    "Bo" : 12,
    "Malene" : 13,
    }
print("\nØvelse 3.6:", student_grades)
print("\nØvelse 3.6:", student_grades.get("Kevin"))
student_grades["Malene"] = 7
# Man kan også bruge update metoden
student_grades.update({"Kevin" : 12})
print(f"\nØvelse 3.6 - opdaterede værdier:\n{student_grades}")