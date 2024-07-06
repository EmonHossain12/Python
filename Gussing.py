import random

RandomNumber= random.randrange(1,200)

UserNumber=int(input("Enter the guessing number:"))

if UserNumber > RandomNumber :
    print(RandomNumber)
    print("This number is too high")
elif UserNumber < RandomNumber :
    print(RandomNumber)
    print("This number is too low")
else : 
    print("Congratulation,Your number is matched")    
  