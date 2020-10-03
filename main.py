import random
def gameWin(com, you):
    if com== you:
      return  False
    elif com== 's':
        if you== 'w':
          return False
        elif you== 'g':
          return True
    elif com== 'w':
        if you== 'g':
          return False
        elif you== 's':
          return  True
    elif com== 'g':
        if you== 's':
          return False
        elif you== 'w':
          return True

print("Computer's turn: Snake(s), Water(w) or Gun(g)?: ")
randNum= random.randint(1, 3)
if randNum== 1:
    com= 's'
elif randNum== 2:
    com= 'w'
elif randNum== 3:
    com= 'g'

you= input("Your turn: Snake(s), Water(w) or Gun(g)?: ")
a= gameWin(com, you)

print(f"Computer has chosen: {com}")
print(f"You have chosen: {you}")

if a== None:
    print("Game tie")
elif a:
    print("You win!")
else:
    print("You lose!")