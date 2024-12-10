# 3 lav en funktion der tager en liste med integers som argument og returnerer en ny liste hvor hvert​
# tal i listen er blevet fordoblet​

binary_values_list = [1, 2, 4, 8, 16, 32]

def double_list_values(inputliste): # tilføj argument​
    returliste=[] # Opret tom ny liste
    for item in inputliste: # For hver ting i den oprindelige liste
        returliste.append(item*2) # Gang tingen med 2 og tilføj det til den tomme liste
    return returliste # Returner den nye liste)

print(double_list_values(binary_values_list)) # test at funktionen virker​
# print output skal vise: [2, 4, 8, 16, 32, 64]​


def double_lst_values(lst):
    return [x*2 for x in lst] # Brug list comprehension i stedet for ovenstående
    
print(double_lst_values(binary_values_list))