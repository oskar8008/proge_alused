suurus = float(input("Sisestage kirja suurus: "))
pealkiri = input("sisestage kirja teema pealkiri: ")
fail = input("kas kirjal on kaasas manus? (y/n): ")
if pealkiri == "" or fail == "y" and suurus > 1:
    print("kiri on spämm")
    
else:
    print("kiri ei ole spämm")