import random

Machine = 0
Shrija = 0
rounds = 5
for i in range(rounds): 
   User = str(input("What do you choose?"))
   choices = ['Rock','Paper','Scissor']
   Computer = random.choice(choices)
   print(Computer)
   if Computer == 'Rock' and User == 'Paper':
        print("You win!")
        Shrija = Shrija + 1
   elif Computer == 'Paper' and User == 'Scissor':
        print ("You win!")
        Shrija = Shrija + 1
   elif Computer ==  'Scissor' and User == 'Rock':
        print("You win!")
        Shrija = Shrija + 1
   elif Computer == 'Rock' and User == 'Scissor':
        print("You lose!")
        Machine = Machine + 1
   elif Computer == 'Paper' and User == 'Rock':
        print("You lose!")
        Machine = Machine + 1
   elif Computer == 'Scissor' and User == 'Paper':
        print("You lose!")
        Machine = Machine + 1
   elif Computer == User:
        print("It's a tie!")
if Machine > Shrija:
    print("I win the match, Shrija!")
elif Machine < Shrija:
    print("Congratulations, Shrija! You won!")
else:
    print("The match is a draw")
    