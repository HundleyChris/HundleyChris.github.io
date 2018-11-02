import turtle
bob = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)
turtle.bgcolor("blue")
r = 20
g = 20
b = 20
for i in range(4):
    bob.color(r,g,b)
    bob.speed(1)
    bob.fd(100)
    bob.rt(90)
    bob.stamp()
    if(g<252):
        g=g+40
        r=r+17
        b=b+70
