import numpy as np
#from matplotlib import pyplot as plt
import sys
import os
    
def card(i, decks, cards): #Card generator
  c = np.ceil(np.random.rand()*(decks*52-i))
  i += 1
  a = 0
  b = None
  for j in range(10):
    a += cards[j]
    if c <= a:
      b = j + 2
      cards[j] -= 1
      break    
  return b, i

def read_value(d1, cards, decks, i): #La bibbia
  #Prob dealer bust
  sys.path.append(os.path.join(os.path.dirname(__file__), 'dealer_prob'))
  from dealer_prob import probd
  sdp, edp, ndp, tdp, tydp, bustdp = probd(d1, cards, decks, i)

  #Prob player bust
  sys.path.append(os.path.join(os.path.dirname(__file__), 'player_prob'))
  from dealer_prob import probp
  spp, epp, npp, tpp, typp, bustpp = probp(c, cards, decks, i)

  #Prob player>dealer
  return

#Variables definition
decks = float(input("Number of decks: "))
depth = float(input("Depth: "))
balance = float(input("Balance: "))
bet = float(input("Bet value: "))
bet1 = bet
counter = 0

while counter < 1: #Cycle every time dealer shuffles deck
  counter += 1

  #Reset deck
  cards = np.empty(10)
  for j in range (10):
    if j == 8:
      cards[j] = decks*16
    else:
      cards[j] = decks*4
  
  i=0

  while True:
    z = 0
    nd = 0

    #Bet setup
    bet = bet1
    balance -= bet

    #Array used for comparing your hand(s) and bet sizes with the dealer
    betar = [] 
    totar = []
    zar = []

    c1, i = card(i, decks, cards)
    d1, i = card(i, decks, cards)
    c2, i = card(i, decks, cards)
    c = c1 + c2



