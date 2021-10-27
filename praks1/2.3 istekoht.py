from random import randint
suva = randint(1,3)
valik1 = input("Kas soovite valida istekoha (ise) või (loosida)? ")
if (valik1 == "ise"):
    valik2 = input("kas soovite istuda (akna) ääres või (mitte)? ")
    if (valik2 == "akna"):
        print("valisite ise akna koha.")
    if (valik2 == "mitte"):
        print("valisite ise koha mitte akna äärde")
 
if suva == 1:
    suva1 = "loosite istekoha ning olete akna ääres"

elif suva == 2 or 3:
    suva1 = "loosisite istekoha ning te ei istu akna ääres"
if (valik1 == "loosida"):
    print(suva1)
    
    

    
    

