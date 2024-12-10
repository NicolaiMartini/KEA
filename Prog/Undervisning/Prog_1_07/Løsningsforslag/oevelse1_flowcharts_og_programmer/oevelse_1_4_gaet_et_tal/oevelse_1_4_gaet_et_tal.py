from random import randint

hemmeligt_tal = randint(1, 10)


while True:
    gaet = int(input("Indtast dit gæt\n>"))
    if gaet == hemmeligt_tal:
        print("Tillykke du gættede rigtigt!")
        break
    else:
        print("Du har gættet forkert, prøv igen!")