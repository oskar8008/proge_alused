def pronksikarva_summa(täisarvud):
    summa = 0
    for münt in täisarvud:
        if int(münt) <= 5:
            summa += int(münt)
    return summa
fail = input("Sisestage failinimi: (mündid.txt) ")
mundid = open(fail + ".txt", encoding="UTF-8")
print("Hoiupõrsasse läheb", pronksikarva_summa(mundid), "senti.")