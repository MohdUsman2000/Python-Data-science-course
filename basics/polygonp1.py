from turtle import *
speed("slowest")
pencolor("red")
bgcolor("pink")
width(10)

side = 3
size = 200
fillcolor("blue")
begin_fill()
for i in range(side):
    fd(size)
    lt(360/side)

end_fill()

mainloop()