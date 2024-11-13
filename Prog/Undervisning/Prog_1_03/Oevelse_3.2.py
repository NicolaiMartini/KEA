# 3.2.3 Opret en tuple med navnet min_tuple, der indeholder følgende elementer: "æble", "banan", "kirsebær".
# Print derefter tuple.
min_tuple=("æble","banan","kirsebær")
print(min_tuple)

# 3.2.4 Brug indeksering til at få adgang til det første og det sidste element i min_tuple.
# Print begge elementer.
print(f"{min_tuple[0]}, {min_tuple[2]}")

# 3.2.5 Opret en ny tuple tal_tuple med tallene 1 til 5.
# Brug slicing til at få en sub-tuple, der indeholder de midterste tre elementer.
tal_tuple=(1,2,3,4,5)
sub_tal_tuple=tal_tuple[1:4]
print(sub_tal_tuple)