import random
print(f"Welcome to the Dice Rolling Game!")

start=input("Do you want to start the game? (y/n):").lower()
if start=="y":
  status=True
elif start=="n":
  status=False
else:
  print("Invalid input. Please input y or n")

while status==True:
  try:
    n=int(input("Enter how many dice you want to roll at a time:"))
    if n>0:
      break
    else:
      print("Enter a positive integer.")
  except ValueError:
    print("Invalid input! Enter a positive integer.")

count=0
while status==True:
  roll=input("Roll the dice? (y/n):").lower()
  if roll=="y":
    output=tuple(random.randint(1, 6) for _ in range(n))
    print(output)
    count+=1
  elif roll=="n":
    break
  else:
    print("Invalid input. Please input y or n")

if count==0:
  print(f"Thank you!\nMaybe next time!")
else:
  print(f"You have rolled {count} times. Thank you for playing!")
