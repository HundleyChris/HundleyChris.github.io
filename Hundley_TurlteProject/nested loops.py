import turtle
bob = turtle.Turtle()
bob.speed(0)
turtle.delay(0)
bob.pu()
bob.goto(-200,-200)
bob.pd()
x=5
def move(x):
    bob.forward(x)
    bob.left(120)
def tri():
    for i in range(3):
        bob.forward(x)
        bob.left(120)
for i in range(3):
    for i in range(3):
        for i in range(3):
            for i in range(3):
                for i in range(3):
                    for i in range(3):
                        for i in range(3):
                            tri()
                            move(x*2)
                        tri()
                        move(x*4)
                    tri()
                    move(x*8)
                tri()
                move(x*16)
            tri()
            move(x*32)
        tri()
        move(x*64)
    tri()
    move(x*128)

