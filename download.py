print('would you like to play a game(yes/no)...')
response=input()
response=response.lower()
if response== 'yes':
    print('Lets play then...')
    game = True
else:
    print("You've made the wrong choice...")
while game == True:
    print('What is your age?')
    num = int(input())
    print('This is your age doubled ' + str(num*2))
    num = int(input("Enter a number:  "))
    if (num % 2) == 0:
       print("{0} is Even".format(num))
    else:
       print("{0} is Odd".format(num))
    game = False
    s = str(input("What pixel size do you want:"))
import turtle
t=turtle.Turlte()
def size(s):
    for i in range(4):
       s t.forward(s)
        t.forward(90)
    
