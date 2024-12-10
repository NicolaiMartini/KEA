# Øvelser med funktioner​

# 4 lav en funktion der tager en liste med integers som argument og omdanner hvert element til​

# en string - Hint brug: str()​

binary_values_list = [1, 2, 4, 8, 16, 32]

def convert_list_values_to_str(liste_der_skal_konverteres):
    str_liste=[] # Opret tom ny liste
    for item in liste_der_skal_konverteres: # For hver ting i den oprindelige liste
        str_liste.append(str(item)) # Gang tingen med 2 og tilføj det til den tomme liste
    return str_liste # Returner den nye liste)

print(convert_list_values_to_str(binary_values_list)) # test at funktionen virker​

# print output skal vise: ['1', '2', '4', '8', '16', '32']​

def convert_lst_values_to_str(lst):
    return [str(x) for x in lst] # Brug list comprehension i stedet for ovenstående

print(convert_lst_values_to_str(binary_values_list))