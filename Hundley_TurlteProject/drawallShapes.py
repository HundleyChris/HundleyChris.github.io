import turtle
bob = turtle.Turtle()
n = int(input("How many sides do you want"))
def AnyRegPoly():
    s = 100
    for i in range(n):
        bob.fd(s)
        bob.rt(360/n)
AnyRegPoly()
 
