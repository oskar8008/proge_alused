from random import randint
pp = int(input("Mitu pöialpoissi tahab õuna?: "))
if pp > 7:
    print("poialpoisse kokku on 7")
    
else:
    a = 0
    õun = 14
    while a < pp:
        a += 1
        rand = randint(1,2)
        õun = õun - rand
        print(str(rand))
    print("lumivalgekesele jäi " + str(õun))

    


    