import random

hemmeligt_nummer = random.randint(1,100)

def faa_gaet_fra_bruger():
    mit_gaet_str = input('Tallet du gætter på: ')
    mit_gaet = int(mit_gaet_str)
    return mit_gaet

bruger_input = []
rigtig_forkert = {}
for i in range(10):
    mit_gaet = faa_gaet_fra_bruger()
    
    bruger_input.append(mit_gaet)
    
    if mit_gaet == hemmeligt_nummer:
        print('Du gættede tallet')
        rigtig_forkert[mit_gaet] = 'Rigtigt'
        break
    elif mit_gaet > hemmeligt_nummer:
        print('Du gættede for højt')
        rigtig_forkert[mit_gaet] = 'Forkert'
    else:
        print('Du gættede for lavt')
        rigtig_forkert[mit_gaet] = 'Forkert'
    
print('Dine gæt:',bruger_input)
print('Dine rigtige og forkerte:',rigtig_forkert)
print(hemmeligt_nummer)