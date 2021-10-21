ainpunk_arv = int(input("sisestage ainepunkdie arv: "))
nädalate_arv = int(input("sisestage nädalate arv: "))
tunde = ainpunk_arv * 26
nädala_ajakulu = round(tunde / nädalate_arv)
print(str(nädala_ajakulu))