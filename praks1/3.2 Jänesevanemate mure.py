ringid = int(input("Mitu ringi olete jooksnud? : "))
a = 1
b = 0
porgandid = 0
while a < ringid:
    a = a + 2
    porgandid = porgandid + 2 + b
    b = b + 2
    
print("Saate kokku " + str(porgandid) + " porgandit!")
