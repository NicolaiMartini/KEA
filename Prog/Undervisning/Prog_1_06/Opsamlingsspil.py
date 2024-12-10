import random

hemmeligt_nummer=random.randint(1,50)

def faa_input_fra_bruger():
    input_str=input('Tast dit gæt:\n>')
    return int(input_str)

bruger_gaet=[]
resultat={}

for i in range(5):
    mit_gaet=faa_input_fra_bruger()
    
    if hemmeligt_nummer==mit_gaet:
        resultat[i+1]='Rigtigt'
        bruger_gaet.append(mit_gaet)
        print('Du gættede rigtigt!')
        break
    else:
        if mit_gaet>hemmeligt_nummer:
            print('Du gættede for højt.')
        else:
            print('Du gættede for lavt.')
        bruger_gaet.append(mit_gaet)
        resultat[i+1]='Forkert'
        
print(f'Her er dine gæt: {bruger_gaet}')
print(f'Resultatet: {resultat}')


input("Press enter to exit.")