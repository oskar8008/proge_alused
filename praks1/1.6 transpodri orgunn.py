inm_arv = int(input("palju inimesi tahab bussi istuda: "))
bussi_kohad = int(input("palju on bussis kohti: "))
bussid = inm_arv // bussi_kohad

maha_jäänud = inm_arv % bussi_kohad
print("maha jäid " + str(maha_jäänud) + " inimest")
print("busse oli " + str(bussid))