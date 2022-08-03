from turtle import *
pensize(3)
pencolor("red")
value = 300
while value > 0: 

    fd(value)
    lt(90)
    value -= 10
    write(value)
mainloop()