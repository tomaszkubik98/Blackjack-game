############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/

from replit import clear
from art import logo
import random

def blackjack():
  print(logo)
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  your_cards=[]
  computers_cards=[]
  current_score=0    
  your_cards.append(random.choice(cards))
  your_cards.append(random.choice(cards))
  computers_cards.append(random.choice(cards))
  computers_cards.append(random.choice(cards))
  
  for card in your_cards:
    current_score+=card
  print(f"My cards: {your_cards}. Your score is {current_score}")
  print(f"Compuer's first card: {computers_cards[0]}")

  def deal_for_comp():
    
    should_draw = True
    while should_draw:
      computers_score=0
      
      for card in computers_cards:
        computers_score+=card
      if computers_score<17:
        new_card=random.choice(cards)
        computers_cards.append(new_card)
        computers_score+=new_card
        
      if computers_score>21 and cards[0] in computers_cards:
        n=0
        for card in computers_cards:
          n+=1
          if card==cards[0]:
            computers_cards[-1]=1
      
      else:       
        should_draw=False
        return computers_score

  def sum_up_score_user():
    score=0
    for card in your_cards:
      score+=card
    return score      
  
  def deal_for_user():
    decision =input("Do you want to draw again 'y' or 'n'? Type: ")
        
    if decision=="n":
      deal_for_comp()
      
    elif decision=="y":
      current_score=0
      your_cards.append(random.choice(cards))
      for card in your_cards:
        current_score+=card
      if current_score>21 and cards[0] in your_cards:
        n=0
        for card in your_cards:
          n+=1
          if card==cards[0]:
            your_cards[-1]=1
        for card in your_cards:
          current_score+=card
        print(f"Your current hand is {your_cards}, your score is {sum_up_score_user()}")
        print(f"Computer's current score is: {computers_cards[0]}")
        deal_for_user()
        
      elif current_score>21:
        deal_for_comp()
        
      elif current_score==21:
        deal_for_comp()
        
      elif current_score<21:
        print(f"Your current hand is {your_cards}, your score is {sum_up_score_user()}")
        print(f"Computer's current score is: {computers_cards[0]}")
        deal_for_user()

  if sum_up_score_user()==21:
    deal_for_comp()
    
  else:        
    deal_for_user()

  def check_who_won():
    if sum_up_score_user()>21:
      return "lost"
    if sum_up_score_user()<=21:
      if sum_up_score_user()==deal_for_comp():
        return "draw"
      elif deal_for_comp()>21:
        return "win"
      elif sum_up_score_user()>deal_for_comp():
        return "win"
      else:
        return "lost"
      
  check_who_won()
  
  if check_who_won()=="lost":
    print(f"Your final hand is {your_cards}, your score is {sum_up_score_user()}\nComputer's final hand is {computers_cards} and his score is: {deal_for_comp()}")
    print("You lose")
  elif check_who_won()=="draw":
    print(f"Your final hand is {your_cards}, your score is {sum_up_score_user()}\nComputer's final hand is {computers_cards} and his score is: {deal_for_comp()}")
    print("Draw")
  else:
    print(f"Your final hand is {your_cards}, your score is {sum_up_score_user()}\nComputer's final hand is {computers_cards} and his score is: {deal_for_comp()}")
    print("You win")

  go_again=input("\n Do you want to go again? Type 'y' or 'n': ")
  if go_again=="y":
    clear()
    blackjack()
      
  
  
  

  
blackjack()
    

