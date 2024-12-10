# Undervisningsgang 3 øvelser

# Øvelse 2
"""
2.3​ Opret en tuple med navnet min_tuple, der indeholder følgende elementer:
"æble", "banan", "kirsebær". Print derefter tuple.​
​​"""
min_tuple = ("æble", "banan", "kirsebær")
print("Øvelse 2.3", min_tuple)

"""
2.4 Brug indeksering til at få adgang til det første og det sidste element i
min_tuple. Print begge elementer.​
​​"""
print("Øvelse 2.4", min_tuple[0], min_tuple[2])

# man få sidste element dynamisk med negativ indeksering
# så vil man altid få det sidste selvom der oprettes en ny tuple med flere ting i
sidste = min_tuple[-1]

# bonus - første og sidste med slicing:
print("Bonus - Første og sidste med slicing", min_tuple[0:3:2])
print("Bonus - Første og sidste med dynamisk slicing", min_tuple[::len(min_tuple)-1])

"""
2.5 Opret en ny tuple tal_tuple med tallene 1 til 5.
Brug slicing til at få en sub-tuple, der indeholder de midterste tre elementer.​
​"""
tal_tuple = (1, 2, 3, 4, 5)
sub_tuple_tal = tal_tuple[1:4] 
print("Øvelse 2.5", sub_tuple_tal)
