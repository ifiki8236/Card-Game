import random

# A card game program using functions and the random library

print("Welcome To Blackjack\n")

print("Here are your cards: ")

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def randomNums1():
  random_num = random.choice(deck)
  return random_num
  
def randomNums2():
  random_num2 = random.choice(deck)
  return random_num2
  
def randomNums3():
  random_num3 = random.choice(deck)
  return random_num3
  
def add2Cards():
  return randomNums1() + randomNums2()
  
def addAllCards():
  return randomNums1() + randomNums2() + third_Card

def checkIfAbove21():
  if firstPlayer_allCards > 21:
    print("Player 1 loses! The sum of your cards were greater than 21.")
  if secondPlayer_allCards > 21: 
    print("Player 2 loses! The sum of your cards were greater than 21.")
    
# def checksWhoIsCloser():
#   if firstPlayer_allCards > secondPlayer_allCards or firstPlayer_allCards > secondPlayer_twoCards or firstPlayer_twoCars > secondPlayer_allCards or firstPlayer_twoCars > secondPlayer_twoCards and firstPlayer_allCards <= 21 or firstPlayer_twoCars <= 21:
#     print("Player 1 wins! You were closer to 21!")
#   elif firstPlayer_allCards < secondPlayer_allCards or firstPlayer_allCards < secondPlayer_twoCards or firstPlayer_twoCars < secondPlayer_allCards or firstPlayer_twoCars < secondPlayer_twoCards and secondPlayer_allCards <= 21 or secondPlayer_twoCards <= 21:
#     print("Player 2 wins! You were closer to 21!")

# def holdWinLossFunctions():
#   return checkIfAbove21(), checksWhoIsCloser()

third_Card = randomNums3()

print("First card is : " + str(randomNums1()))
print("Second card is : " + str(randomNums2()))
firstPlayer_twoCars = add2Cards()
player_1_hitStand = (input("Player 1 - hit or stand: "))
print("\n")
firstPlayer_allCards = addAllCards()


print("First card is : " + str(randomNums1()))
print("Second card is : " + str(randomNums2()))
secondPlayer_twoCards = add2Cards()
player_2_hitStand = (input("Player 2 - hit or stand: "))
secondPlayer_allCards = addAllCards()

if player_1_hitStand == "hit":
  print("Third card is : " + str(third_Card))
  print("Player 1 - Your hand is:", firstPlayer_allCards)
elif player_1_hitStand =='stand':
  print('Player 1 - Your hand is:',firstPlayer_twoCars)

if player_2_hitStand == "hit":
  print("Third card is : " + str(third_Card))
  print("Player 2 - Your hand is:", addAllCards())
elif player_2_hitStand =='stand':
  print('Player 2 - Your hand is:',secondPlayer_twoCards)

# announce_Winner_or_Loser = holdWinLossFunctions()