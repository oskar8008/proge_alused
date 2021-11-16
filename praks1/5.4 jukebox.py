fail = open(input("Sisestage playlisti nimi: jukebox.txt / 88ndad.txt / eesti_muusika.txt / edm.txt  "), encoding="UTF-8")
laul = 1
print("laulude valik: ")
loend = []
for rida in fail:
    print(str(laul) + " " + str(rida[:-1]))
    laul += 1
    loend. append(rida)
lauluvalimine = int(input("valige laulu number: "))
lauluvalimine -= 1
print("präegu mängib " + loend[lauluvalimine])
fail.close()

