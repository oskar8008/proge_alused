def banner(lause):
    return lause.upper()
korda = int(input("mitu korda soovite reklaamlasuset kuvada? "))
lause = input("sisestage reklaamlause: ")
for i in range(0, korda):
    print(banner(lause))