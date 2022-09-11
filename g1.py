import pgzrun 

HEIGTH =500
WIDTH = 600
p = Actor("ironman", pos=(100,100))
def draw():
    screen.clear()
    screen.draw.text("Welcome to pgzero", (10,10), color = 'red', fontsize=50)
    screen.draw.text("created by mohd usman ", (10,300), color="white")
    p.draw()
#outside function
pgzrun.go()