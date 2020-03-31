import random
from db import insertOutcome, onQuit, getMostUsedWeapon

def chooseWeapon(choice):
    weapons = ("rock", "paper", "scissors")
    return weapons[choice]

def checkOutcome(aiWeapon, playerWeapon):
    if aiWeapon == playerWeapon:
        print("AI chose " + aiWeapon)
        print("TIE")
        insertOutcome(playerWeapon, aiWeapon, "TIE")
    elif (aiWeapon == "rock" and playerWeapon == "scissors") or (aiWeapon == "scissors" and playerWeapon == "paper") or (aiWeapon == "paper" and playerWeapon == "rock"):
        print("AI chose " + aiWeapon)
        print("You Lose")
        insertOutcome(playerWeapon, aiWeapon, "LOST")
    elif (aiWeapon == "scissors" and playerWeapon == "rock") or (aiWeapon == "paper" and playerWeapon == "scissors") or (aiWeapon == "rock" and playerWeapon == "paper"):
        print("AI chose " + aiWeapon)
        print("You Win")
        insertOutcome(playerWeapon, aiWeapon, "WON")
    else:
        print("ERROR TRY AGAIN " + playerWeapon + " " + aiWeapon)

def playerDecides():
    playerInquery = input("Rock, Paper, Scissors or (quit)? ")
    if playerInquery.lower() == "rock":
        return chooseWeapon(0)
    elif playerInquery.lower() == "paper":
        return chooseWeapon(1)
    elif playerInquery.lower() == "scissors":
        return chooseWeapon(2)
    elif playerInquery.lower() == "quit":
        print("Quitting Game")
        return playerInquery.lower()
    else:
        print("FAILED TRY AGAIN")

def aiDecides(aiLevel):
    if(aiLevel == "2"):
        # Level 2 (REMEMBERS YOUR LEAST PICKED WEAPON)
        return getMostUsedWeapon()
    else:
        # Level 1 (RANDOM)
        rand = random.randint(0,2) # Chose rock paper scissor
        return chooseWeapon(rand)

def gameMain():
    playerWeapon = ""
    aiLevel = input("Choose level of difficulty (1 or 2) ")
    while playerWeapon != "quit":
        aiWeapon = aiDecides(aiLevel)
        playerWeapon = playerDecides()
        checkOutcome(aiWeapon, playerWeapon)
    onQuit()

if __name__ == "__main__":
  print("Starting") 
  gameMain() 
  print("GAME OVER")