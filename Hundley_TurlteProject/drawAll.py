import turtle
bob = turtle.Turtle()
turtle.colormode(255)
turtle.color(0,0,0)
turlte.bgcolor(135,0,0)
def dec():
    for i in range(11):
        bob.fd(100)
        bob.rt(33)
def hexa():
    for i in range(6):
        bob.fd(100)
        bob.rt(60)
def nan():
    for i in range(9):
        bob.fd(100)
        bob.rt(40)
def pent():
    for i in range(5):
        bob.fd(100)
        bob.rt(72)
def square():
    for i in range(4):
        bob.speed(1)
        bob.fd(100)
        bob.rt(90)
def tri():
    for i in range(3):
        bob.fd(100)
        bob.rt(120)
