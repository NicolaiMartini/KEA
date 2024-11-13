# -*- coding: utf-8 -*-

#Variabler
dyr = "ko"
print(type(dyr))

yndlings_primtal = 19
print(type(yndlings_primtal))

tal_som_str = '123'
print(type(tal_som_str))
tal_som_int = int(tal_som_str)
print(tal_som_str, tal_som_int, type(tal_som_int))

#Pas på når man ligger tal sammen
print('1'+'1')
print(1 + 1)

#Dynamic typing
a = 1
print(type(a))
a = 'Hej'
print(type(a))
a = True
print(type(a))

#Boolean logic
a = 3
b = 5
print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print(a > b or a <= b)
print(a > b and a == b)

#For loops
listen_af_tal = list(range(10))
for i in listen_af_tal:
    print(i, end=', ')
print()

for i in range(3):
    print('Programmering er sjovt')

#Break i for loops
for i in range(3000):
    print(i,'Programmering er super sjovt')
    if i > 5:
        break

#Nested for loops
for i in range(0, 11):
    for j in range(0, 11):
        print(i * j, end=', ')
    print()
    
#While loop
a = 10
while a > 0:
    print(a)
    a = a - 1

'''
while True:
    print('Programmering er for evigt')
'''

#Også et for evigt loop
'''
a = 10
while a > 0:
    print(a)
'''

'''
while True:
    if trykket_paa_knappen:
        break
    print('Der er ikke trykket på knappen')
'''

a = 0
while True:
    a += 1 # a = a + 1
    if a > 10:
        break
print(a)

#Functions
def add(a1, a2):
    return a1+a2

def add_print(a1, a2):
    print(a1+a2)

print(add(1,2))
add_print(1,2)

resultat1 = add(1,2)
resultat2 = add_print(1,2)

print('Resultat1:',resultat1)
print('Resultat2:',resultat2)

# ''' danner en multilinje streng
#som kan bruges til at kommentarer ud
multilinje = '''
asdfsadf
asdfsadf
asdfasdf
'''
print(multilinje)

#Collections types (sequence types)
#Lister
liste1 = ['Banan', 'Æble', 'Pære']
print(liste1)
#Tilføj til listen (Append = Apply to End)
liste1.append('Blomme')
print(liste1)
#Tilgå og ændre en liste ud fra index
print(liste1[0])
liste1[1] = 'Jordbær'
print(liste1)
#Slicing - vi tager en bid af listen
print(liste1[1:3])
liste1.append('Æble')
print(liste1)
#Tag hver anden
print(liste1[0:6:2])
#Vender listen om (listen i omvendt rækkefølge)
print(liste1[::-1])
#Tilføj midt i en liste
liste1.insert(2, 'Kiwi')
print(liste1)

#Tuples
tupple1 = (1,2,3)
print(tupple1)
print(tupple1[1])

#Vi kan ikke append
#tupple1.append(4)

#Vi kan ikke ændre en tupple
#tupple1[1] = 6

#vi kan godt slice ligesom en liste
print(tupple1[::-1])

def funk_der_returnere_tupple():
    return ('a','b','c')

print(funk_der_returnere_tupple())
#Destructing bind / Vi pakker værdierne i tupplen om til variabler
var1, var2, var3 = funk_der_returnere_tupple()
print(var1,var2,var3)

#Dicts / Dictonary
bil1 = {'navn': 'Skoda',
        'model': 'Superb',
        'year': 2023}
print(bil1)
#Tilgå dict
print(bil1['navn'])

#ændre dict
bil1['model'] = 'Fabia'

print(bil1)

print(bil1.get('year'))

#Resultere i fejl
#print(bil1['Ejer'])

#Returnere None hvis nøglen ikke findes i dictonary
print(bil1.get('Ejer'))

#Class and objects (object orienteret programmering)
class Person:
    def __init__(self):
        self.navn = ''
        self.alder = 0
        self.land = ''
        
    def beskrivelse(self):
        print(f'{self.navn} er {self.alder} år gammel og kommer fra {self.land}')
        
nat = Person()
nat.navn = 'Kevin'
nat.alder = 31
nat.land = 'Danmark/Italien'
nat.beskrivelse()
















'''
#Primtalsfinder. Bruger at else til et for loop bliver udført
#hvis der ikke bliver kaldt break fra for loop'et
primtal = [2]
for i in range(3,30):
    for j in primtal:
        if i%j == 0:
            break
    else:
        primtal.append(i)
print(primtal)
'''