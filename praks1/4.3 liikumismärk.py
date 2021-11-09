from tkinter import *
 
raam = Tk()
raam.title("ohum2rk")
# loome tahvli laiusega 880px ja kõrgusega 560px
tahvel = Canvas(raam, width=1000, height = 1000)
tahvel.create_polygon(500,20,20,900,980,900, fill="yellow", width=30,
outline="red")
tahvel.create_rectangle(450,200,550,600, fill="black")
tahvel.create_rectangle(450,650,550,750, fill="black")

tahvel.pack()
raam.mainloop()