import random

# SNAKE ,WATER ,GUN or rock paper scissor

def gameWin(comp , you):
    if comp == you:
        return None
    elif  comp =='s':
     if  you =='w':
        return False
    elif you =='g':
        return True
    elif comp == 'w':
        if you =='g':
            return False
        elif you =='s':
            return True
    elif comp =='g':
        if you =='s':
            return False
        elif you=='w':
            return True

print("comp Turn : Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = "g"
you = input("your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"computer choose {comp}")  # by using f string we can choose variable
print(f" you choose {you}")

if a == None:
    print("THE GAME IS A TIE!")
elif a :
    print("YOU WIN")
else:
    print("YOU LOSE!")
