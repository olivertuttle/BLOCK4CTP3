import random

print("Hello! What kind of die do you want to roll?")
dieType = input("Type d20, d12, d8, d6, or d4:  ")
print("Thank you! Here's your roll: ")

#if a d20 is selected, pick a random number between 1 and 20
#we're using random.randint(x , y)


if dieType.lower() == "d20":
   print(random.randint(1, 20))

elif dieType.lower() == "d12":
   print(random.randint(1, 12))

elif dieType.lower() == "d8":
   print(random.randint(1, 8))

elif dieType.lower() == "d6":
   print(random.randint(1, 6))

elif dieType.lower() == "d4":
   print(random.randint(1, 4))

else:
    print("hey dont do that, loser")

