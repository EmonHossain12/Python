import random

options=['Rock','Paper','Scissors']

user_choice=input("Enter your choice:")
computer_choice=random.choice(options)

print("Your choice:",user_choice)
print("Computer choice:",computer_choice)

if user_choice == computer_choice :
    print("It's a tie !")
elif user_choice =='Rock' and computer_choice == 'Scissors': 
     print("You are win !")
elif user_choice == 'Paper' and computer_choice == 'Rock':
      print("You are win")    
elif user_choice == 'Scissors' and computer_choice == 'Paper':
           print("You are win")   
else :
       print("Computer wins !")