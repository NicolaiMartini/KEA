# 3.3.2 Opret en dictionary frugt_priser, der indeholder priserne på forskellige frugter.
# Brug get-metoden til at hente prisen på en frugt, der findes i dictionaryen, og en frugt, der ikke findes.
frugt_priser={"æble":5,"banan":7,"kirsebær":8}
print(f"3.3.2, {frugt_priser.get('æble')}")

# 3.3.3 Opdater prisen på en frugt i frugt_priser dictionaryen.
frugt_priser["æble"]=6
print(f"3.3.3, {frugt_priser}")

# 3.3.4 Brug values-metoden til at få en liste over alle værdierne i frugt_priser dictionaryen.
print(f"3.3.4, {frugt_priser.values()}")

# 3.3.5 Brug keys-metoden til at få en liste over alle nøglerne i frugt_priser dictionaryen.
print(f"3.3.5, {frugt_priser.keys()}")

# 3.3.6 Opret en dictionary student_grades med nogle studenter og deres karakterer.
# Brug get-metoden til at hente en students karakter, opdater en students karakter, og brug values og keys metoderne til at få alle karakterer og alle studentnavne.
student_grades={"Kim":7,"Anna":9,"Peter":12,"Jonathan":5}
print(f"3.3.6, {student_grades['Kim']}")
student_grades["Anna"]=8
print(f"3.3.6, {student_grades['Anna']}")
print(f"3.3.6, {student_grades.keys()}")
print(f"3.3.6, {student_grades.values()}")