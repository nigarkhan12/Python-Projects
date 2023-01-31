# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
'''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|          

'''

scissors = '''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

'''

gameImages = [rock, paper, scissors]

userChoice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, You Lose")
else:
    print(gameImages[userChoice])

computerChoice = random.randint(0, 2)
print("Computer Chose:")
print(gameImages[computerChoice])


if userChoice == 0 and computerChoice == 2:
    print("You Win!")
elif computerChoice == 0 and userChoice == 2:
    print("You Lose")
elif computerChoice > userChoice:
    print("You Lose")
elif userChoice > computerChoice:
    print("You Win!")
elif computerChoice == userChoice:
    print("It's a draw")