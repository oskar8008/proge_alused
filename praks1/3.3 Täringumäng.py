from random import randint
arv = int(input("täringute arv: "))
a = 0
while a < arv:
    rand = randint(1,6)
    a += 1
    print(str(rand))
          