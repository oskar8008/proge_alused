def mahlapakkide_arv(õunte_kogus):
    ans = round(õunte_kogus*0.4 / 3)
    return ans

kilo = float(input("mitu kilogrammi õunu on? "))
print(mahlapakkide_arv(kilo))