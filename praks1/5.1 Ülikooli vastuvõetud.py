fail = open("rebased.txt", encoding="UTF-8")
aasta = int(input("Mis aasta andmeid vajate: "))
aasta1 = 2011
if aasta >= 2020 or aasta <= 2010:
    print(aasta, "aasta kohta ei ole veel andmeid")
    
for rida in fail:
    if aasta == aasta1:
        print(aasta1, " aastal oli vastuvõetuid ", rida)
        break
    aasta1 += 1
    
fail.close()
