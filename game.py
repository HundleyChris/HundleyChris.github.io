print('Would you like to play a game(yes/no)...')
response=input()
response=response.lower()
if response == 'yes' or response=='y':
    game = True
    print('Lets go...')

print('You start out in a abandoned warehouse.')
print('What do you do...')
print('A.Leave through the front door.')
print('B.Find the reason why you are there.')

response=input()
response=response.upper()
if response == 'A':
    print('You escape safely.')

if response == 'B':
    print('You go into the celler that smells nasty.')
    print('You see a dead body with a note on it.')
    print('Do you read it (yes/no)')
response=input()
response=response.lower()
if response == 'no':
    print('You get shot in the head')

if response == 'yes':
    print('It says your clone is going to kill you.')
    print('You get shot in the head.')
    

        
    game = False
