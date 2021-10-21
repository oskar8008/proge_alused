nimi = input("sisestage oma nimi: ")
lub_kiirus = int(input("sisestage lubatud kiirus: "))
teg_kiirus = int(input("sisestage tegelik kiirus: "))
ületatud_kiirus = (teg_kiirus - lub_kiirus)
kesk = (", kiiruse ületamise eest on teie trahv ")
lõpp = (" eurot")
trahv = ületatud_kiirus * 3
trahv_min = min(190, trahv) 
lause = str(nimi) + kesk + str(trahv_min) + lõpp
print(lause)
