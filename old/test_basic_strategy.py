import numpy as np
#from matplotlib import pyplot as plt

def read_value(filepath, row_x, column_y, TC): #Basic strategy + modifies
  with open(filepath, 'r') as file:
      for i, line in enumerate(file):
          if i == row_x - 1:  
              value = line.strip().split()
              if column_y - 1 < len(value):  
                  return value[column_y - 1]
              else:
                  return None
  return None


def card(RC, i, decks, cards): #Card counting
  i += 1
  c = np.ceil(np.random.rand()*(decks*52-i))
  a = 0
  b = None
  for j in range(10):
    a += cards[j]
    if c < (a + 1):
      b = j + 2
      cards[j] -= 1
      break

  if b in [2, 3, 4, 5, 6]:
    RC += 1.0
  elif b in [10, 11]:
    RC -= 1.0
  TC = RC / (decks - i/52)
  #print (b, decks*52-i, TC) #Bug fixing

  return b, RC, i, TC


def scenario_1(balance, bet, value, s, d1, tot, RC, TC, i, decks, cards, nd): #Scenario 1
  while True:
    if (value == "H"): #Hit
      pass
    elif (value == "S"): #Stand
      break
    elif (value == "D"): #Double otherwise hit
      if (balance >= bet and nd != 1): #Double
        balance -= bet
        bet *= 2
        c, RC, i, TC = card(RC, i, decks, cards)

        if (s > 10 and c == 11): #Ace value 1
          tot += 1
        else:
          tot += c
        break
      else: #Hit
        pass
    elif (value == "U"):
      break
    else: #Error
      print("\033[95mError\033[0m")
      break

    while True: #Additional cards if hit
      c, RC, i, TC = card(RC, i, decks, cards)

      if (s > 10 and c == 11): #Ace value is 1 if my hand value is 11 or above
        c = 1

      if (s+c > 21): #Bust condition
        tot += c
        break

      if (c != 11): #New card is not an ace with value 11
        s += c
        tot += c
        value = read_value("S2_2.txt", row_x = s, column_y = d1, TC = TC)
        if (value == "H"): #Hit
          pass
        elif (value == "S"): #Stand
          break
        elif (value == "D"): #Double otherwise hit
          if (balance >= bet and nd != 1): #Double
            c, RC, i, TC = card(RC, i, decks, cards)
            balance -= bet
            bet *= 2

            if (s > 10 and c == 11): #Ace value 1
              tot += 1
            else:
              tot += c
            break
          else: #Hit
            pass
        else: #Error
          print("\033[95mError\033[0m")
          break
      
      if (c == 11): #New card is an ace with possible value 11
        value = read_value("S3_2.txt", row_x = s, column_y = d1, TC = TC)
        if (value == "H"): #Hit
          pass
        elif (value == "S"): #Stand
          tot += c
          break
        elif (value == "D"): #Double otherwise hit
          if (balance >= bet and nd != 1): #Double
            c, RC, i, TC = card(RC, i, decks, cards)
            balance -= bet
            bet *= 2

            if (c == 11): #Ace has value 1 beacuse there already is an ace
              tot += 1
            else:
              tot += c

            if (tot > 10): #If the sum of the cards is > 10, the 3d card (ace) must be valued 1
              tot += 1
            else: #If the sum of the cards is < 11, the 3d card (ace) must be valued 11
              tot += 11
            break
          else: #Hit
            pass
        elif (value == "G"): #Double otherwise stand
          if (balance >= bet and nd != 1): #Double
            c, RC, i, TC = card(RC, i, decks, cards)
            balance -= bet
            bet *= 2

            if (c == 11): #Ace has value 1 beacuse there already is an ace
              tot += 1
            else:
              tot += c

            if (tot > 10): #If the sum of the cards is > 10, the 3d card (ace) must be valued 1
              tot += 1
            else: #If the sum of the cards is < 11, the 3d card (ace) must be valued 11
              tot += 11            
            break
          else: #Stand
            break
        else: #Error
          print("\033[95mError\033[0m")
          break

        while True: #New cards if hit
          c, RC, i, TC = card(RC, i, decks, cards)

          if (c == 11): #Aces must be valued 1
            c = 1
          s += c
          tot += c

          if ((s+1) > 21): #Bust condition
            tot += 1
            break
          
          if (s < 11): #Condition that 3d card is an ace and can be valued 11
            value = read_value("S3_2.txt", row_x = s, column_y = d1, TC = TC)
            if (value == "H"): #Hit
              pass
            elif (value == "S"): #Stand
              break
            elif (value == "D"): #Double otherwise hit
              if (balance >= bet and nd != 1): #Double
                c, RC, i, TC = card(RC, i, decks, cards)
                balance -= bet
                bet *= 2

                if (c == 11): #Aces must be valued 1
                  tot += 1
                else:
                  tot += c 

                if (tot > 10): #If the sum of the cards is > 10, the 3d card (ace) must be valued 1
                  tot += 1
                else: #If the sum of the cards is < 11, the 3d card (ace) must be valued 11
                  tot += 11
                break
              else: #Hit
                pass
            elif (value == "G"): #Double otherwise stand
              if (balance >= bet and nd != 1): #Double
                c, RC, i, TC = card(RC, i, decks, cards)
                balance -= bet
                bet *= 2

                if (c == 11): #Aces must be valued 1
                  tot += 1
                else:
                  tot += c

                if (tot > 10): #If the sum of the cards is > 10, the 3d card (ace) must be valued 1
                  tot += 1
                else: #If the sum of the cards is < 11, the 3d card (ace) must be valued 11
                  tot += 11
                break
              else: #Stand
                break
            else: #Error
              print("\033[95mError\033[0m")
              break

          if (s > 10): #Condition that 3d card is an ace and has value 1
            s += 1 #Add one because the 3d is an ace of value 1
            tot += 1
            while True:
              value = read_value("S2_2.txt", row_x = s, column_y = d1, TC = TC)
              if (value == "H"): #Hit
                pass
              elif (value == "S"): #Stand
                break
              elif (value == "D"): #Double otherwise hit
                if (balance >= bet and nd != 1): #Double
                  c, RC, i, TC = card(RC, i, decks, cards)
                  balance -= bet
                  bet *= 2

                  if (c == 11): #Aces must be valued 1
                    tot += 1
                  else:
                    tot += c
                    break
                else: #Hit
                  pass
              else: #Error
                print("\033[95mError\033[0m")
                break
              
              #New card if Hit
              c, RC, i, TC = card(RC, i, decks, cards)                
              s += c
              tot += c

              if (s > 21): #Bust conditon
                break
            break
        break
    break
  
  return balance, bet, d1, tot, RC, TC, i


def scenario_2(balance, bet, s, d1, tot, RC, TC, i, decks, cards, nd): #Scenario 2
  while True:
    value = read_value("S3_2.txt", row_x = s, column_y = d1, TC = TC)

    if (value == "H"): #Hit
      pass
    elif (value == "S"): #Stand
      if (tot > 10): #We must add the ace value
        tot += 1
      else:
        tot += 11
      break
    elif (value == "D"): #Double otherwise hit
      if (balance >= bet and nd != 1): #Double
        c, RC, i, TC = card(RC, i, decks, cards)
        balance -= bet
        bet *= 2

        if (c == 11): #If an ace is drawn, it's value must be 1
          tot += 1
        else:
          tot += c

        if (tot > 10): #We must add the ace value
          tot += 1
        else:
          tot += 11
        break
      else: #Hit
        pass
    elif (value == "G"): #Double otherwise stand
      if (balance >= bet and nd != 1): #Double
        c, RC, i, TC = card(RC, i, decks, cards)
        balance -= bet
        bet *= 2

        if (c == 11): #If an ace is drawn, it's value must be 1
          tot += 1
        else:
          tot += c

        if (tot > 10): #We must add the ace value
          tot += 1
        else:
          tot += 11
        break    
      else: #Stand
        if (tot > 10): #We must add the ace value
          tot += 1
        else:
          tot += 11
        break    
    else: #Error
      print("\033[95mError\033[0m")
      break

    while True:
      c, RC, i, TC = card(RC, i, decks, cards)
        
      if (c == 11): #If an ace is drawn, it's value must be 1
        c = 1
      s += c
      tot += c
      
      if ((s + 1) > 21): #Bust condition. Added 1 for the 1st(2nd) ace
        tot += 1
        break

      if (s < 11): #Ace can be valued 11
        value = read_value("S3_2.txt", row_x = s, column_y = d1, TC = TC)
        if (value == "H"): #Hit
          pass
        elif (value == "S"): #Stand
          if (tot > 10): #We must add the ace value
            tot += 1
          else:
            tot += 11
          break
        elif (value == "D"): #Double otherwise hit
          if (balance >= bet and nd != 1): #Double
            c, RC, i, TC = card(RC, i, decks, cards)
            balance -= bet
            bet *= 2

            if (c == 11): #If an ace is drawn, it's value must be 1
              tot += 1
            else:
              tot += c

            if (tot > 10): #We must add the ace value
              tot += 1
            else:
              tot += 11
            break        
          else: #Hit
            pass
        elif (value == "G"): #Double otherwise stand
          if (balance >= bet and nd != 1): #Double
            c, RC, i, TC = card(RC, i, decks, cards)
            balance -= bet
            bet *= 2

            if (c == 11): #If an ace is drawn, it's value must be 1
              tot += 1
            else:
              tot += c

            if (tot > 10): #We must add the ace value
              tot += 1
            else:
              tot += 11
            break        
          else: #Stand
            if (tot > 10): #We must add the ace value
              tot += 1
            else:
              tot += 11
            break
        else: #Error
          print("\033[95mError\033[0m")
          break

      if (s > 10): #Ace must be valued 1
        s += 1 #Adding ace value (1st or 2nd card)
        tot += 1
        while True:
          value = read_value("S2_2.txt", row_x = s, column_y = d1, TC = TC)
          if (value == "H"): #Hit
            pass
          elif (value == "S"): #Stand
            break
          elif (value == "D"): #Double otherwise hit
            if (balance >= bet and nd != 1): #Double
              c, RC, i, TC = card(RC, i, decks, cards)
              balance -= bet
              bet *= 2

              if (c == 11): #If an ace is drawn, it's value must be 1
                tot += 1
              else:
                tot += c
              break          
            else: #Hit
              pass
          else: #Error
            print("\033[95mError\033[0m")
            break
          
          c, RC, i, TC = card(RC, i, decks, cards)
            
          s += c
          tot += c
          if (s > 21): #Bust condition
            break  
        break
    break
  return balance, bet, d1, tot, RC, TC, i


#Variables definition
#decks = float(input("Number of decks: "))
decks = 8
#depth = float(input("Depth: "))
depth = 0.2
#balance = float(input("Balance: "))
balance = 10000
#bet = float(input("Bet value: "))
bet = 1
bet1 = bet
w = 0.
l = 0.
bj = 0.
dr = 0.
xgraph = []
ygraph = []
counter = 0
nd = 0


np.random.seed(5)

while counter < 100000: #Cycle every time dealer shuffles deck

  #Card dealing setup
  cards = np.empty(10)
  for j in range (10):
    if j == 8:
      cards[j] = decks*16
    else:
      cards[j] = decks*4

  #True count setup
  RC = 0.
  i = 0.

  while True: #Cycle every time a play is made
    counter += 1
    z = 0
    nd = 0

    #Bet setup
    bet = bet1
    balance -= bet

    #Final counting. Method to use if have a split, otherwise loss of first hand bet and value
    betar = [] 
    totar = []
    zar = []

    c1, RC, i, TC = card(RC, i, decks, cards)
    d1, RC, i, TC = card(RC, i, decks, cards)
    c2, RC, i, TC = card(RC, i, decks, cards)
    d2, RC, i, TC = card(RC, i, decks, cards)

    if ((d1 + d2) == 21 and (c1 + c2) != 21):
      tot = 1
      totar.append(tot)
      betar.append(bet)
      zar.append(z)
      pass
    else:

      #Scenario 1
      if (c1 != c2 and c1 != 11 and c2 != 11):
        s = c1 + c2
        tot = s

        value = read_value("S2_2.txt", row_x = s, column_y = d1, TC = TC)
      
        balance, bet, d1, tot, RC, TC, i = scenario_1(balance, bet, value, s, d1, tot, RC, TC, i, decks, cards, nd)

        totar.append(tot)
        betar.append(bet)
        zar.append(z)


      #Scenario 2
      if (c1 != c2 and (c1 == 11 or c2 == 11)):
        if (c1 == 11): #Card 1 is an ace
          s = c2
          tot = c2       
        else: #Card 2 is an ace
          s = c1
          tot = c1
        balance, bet, d1, tot, RC, TC, i = scenario_2(balance, bet, s, d1, tot, RC, TC, i, decks, cards, nd)
        totar.append(tot)
        betar.append(bet)
        zar.append(z)


      #Scenario 3
      if (c1 == c2):
        value = read_value("S1_2.txt", row_x = c1, column_y = d1, TC = TC)
        if (value == "Y"): #Split
          balance -= bet
          nd = 1
          for x in range (2):
            c, RC, i, TC = card(RC, i, decks, cards)
            bet = bet1
            z = 0

            if (c1 != 11  and c != 11): #Scenario 1
              s = c1 + c
              tot = s
              value = read_value("S2_2.txt", row_x = s, column_y = d1, TC = TC)
              balance, bet, d1, tot, RC, TC, i = scenario_1(balance, bet, value, s, d1, tot, RC, TC, i, decks, cards, nd)
              totar.append(tot)
              betar.append(bet)
              zar.append(z)

            if ((c1 + c) == 21): #Blackjack condition
              tot = c1 + c
              z = 1
              totar.append(tot)
              betar.append(bet)
              zar.append(z)

            if ((c1 == 11 or c == 11) and (c1 + c) != 21): #Scenario 2
              if (c1 == 11 and c != 11): #Card 1 is an ace
                s = c
              elif (c1 == 11 and c == 11):
                s = 1     
              elif (c == 11 and c1 != 11): #Card 2 is an ace
                s = c1
              tot = s

              if s == 1:
                c, RC, i, TC = card(RC, i, decks, cards)

                if c == 11:
                  c = 1
                
                tot += c

                if (tot + 11) < 22:
                  tot += 11
                else:
                  tot += 1
              else:
                balance, bet, d1, tot, RC, TC, i = scenario_2(balance, bet, s, d1, tot, RC, TC, i, decks, cards, nd)

              totar.append(tot)
              betar.append(bet)
              zar.append(z)


        elif (value == "N"): #No split -> scenario 1 
          s = c1 + c2
          tot = s
          value = read_value("S2_2.txt", row_x = s, column_y = d1, TC = TC)
          balance, bet, d1, tot, RC, TC, i = scenario_1(balance, bet, value, s, d1, tot, RC, TC, i, decks, cards, nd)
          totar.append(tot)
          betar.append(bet)
          zar.append(z)


    dtot = d1 + d2
    #print (totar) #Bug fixes

    #Blackjack draw condition 
    for k in range (len(zar)):
      if (((c1 + c2) == 21 or zar[k] == 1) and dtot == 21):
        balance += betar[k]
        d += 1
        totar[k] -= totar[k]

    #Blackjack condition 
    for k in range (len(zar)):
      if ((zar[k] == 1 or (c1 + c2) == 21) and dtot != 21):
        balance += betar[k]*2.5
        bj += 1
        totar[k] -= totar[k]

    #Dealer blackjack condition 
    for k in range (len(zar)):
      if (dtot == 21 and (zar[k] != 1 or (c1 + c2) != 21)):
        l += 1
        totar[k] -= totar[k]

    #Bust condition
    for k in range (len(zar)):
      if (totar[k] > 21):
        l += 1
        totar[k] -= totar[k]

    #Dealer cards, soft 17 (only if not bj)
    check = 0
    for k in range (len(zar)):
      if totar[k] != 0:
        check = 1

    if (check == 1):
      if (d1 == 11 or d2 == 11):
        if (d1 == 11 and d2 == 11):
          dtot = 1
        elif (d1 == 11 and d2 != 11):
          dtot = d2
        else:
          dtot = d1

        if ((dtot + 11) > 16 and (dtot + 11) < 22): #Stand condition for dealer, ace value is 11
          pass
        
        while True:
          d, RC, i, TC = card(RC, i, decks, cards)

          if d == 11:
            d = 1
          
          dtot += d

          if ((dtot + 11) > 16 and (dtot + 11) < 22): #Dealer betweeen 17 and 21
            dtot += 11
            break
          
          if ((dtot + 1) > 16): #Dealer stand or bust condition with ace value 1
            dtot += 1
            break
          
          if (dtot > 10): #Ace value must be 1
            dtot += 1
            while True:
              d, RC, i, TC = card(RC, i, decks, cards)

              if d == 11:
                d = 1
              
              dtot += d

              if (dtot > 16): #Dealer stop condition
                break
            break
      else:
        dtot = d1 + d2

        if (dtot > 16): #No more cards needed
          pass
        else:
          while True:
            d, RC, i, TC = card(RC, i, decks, cards)

            if (d != 11):
              dtot += d
            elif (d == 11 and dtot > 10):
              d = 1
              dtot += d
            else:
              if ((dtot + 11) > 16 and (dtot + 11) < 22): #Dealer stand condition, ace value 11
                dtot += 11
                break

              if ((dtot +1) > 16): #Dealer stand or bust condiotion, ace value 1
                dtot += 1
                break
              
              while True:
                d, RC, i, TC = card(RC, i, decks, cards)

                if d == 11:
                  d +=1
                
                dtot += d
              
                if ((dtot + 11) > 16 and (dtot + 11) < 22): #Dealer betweeen 17 and 21
                  dtot += 11
                  break
                
                if ((dtot + 1) > 16): #Dealer stand or bust condition with ace value 1
                  dtot += 1
                  break
                
                if (dtot > 10): #Ace value must be 1
                  dtot += 1
                  while True:
                    d, RC, i, TC = card(RC, i, decks, cards)

                    if d == 11:
                      d = 1
                    
                    dtot += d

                    if (dtot > 16): #Dealer stop condition
                      break
                  break
              break
            
            if dtot > 16:
              break

    #Dealer bust condition
    if dtot > 21:
      balance += 2*bet
      w += 1
    
    #General win/lose/draw condition
    for k in range (len(totar)):
      if (totar[k] != 0 and dtot < 22 and totar[k] > dtot):
        balance += 2*betar[k]
        w += 1
      elif (totar[k] != 0 and dtot < 22 and totar[k] < dtot):
        l += 1
      elif (totar[k] != 0 and dtot < 22 and totar[k] == dtot):
        balance += betar[k]
        dr += 1
    

    #print (totar) #Bug fixing
    #print (dtot)
    #print (balance)
    #print ("-----------------------------------")
    #zz = input ("New draw? ") 
    #if (zz == ("no" or "No")):
    #  break

    ygraph.append(balance)
    xgraph.append(counter)

    #Cheks if the deck has enough cards    
    if (decks*52 - i) <= (decks*52*depth):
      break

  #zz = input ("New deck? ")
  #if (zz == ("no" or "No")):
  #  break

#Results calculations
print ("New balance is: ", balance)
#print ("Numero di giocate: ", counter)
#print ("Win prob: ", w/(w+l+bj+dr)*100)
print ("Loss prob: ", l/(w+l+bj+dr)*100)
print ("Blackjack prob: ", bj/(w+l+bj+dr)*100)
print ("Draw prob: ", dr/(w+l+bj+dr)*100)
print ("Win: ", (w+bj)/(w+l+bj+dr)*100)

#plt.plot(xgraph, ygraph, label = "Balance")
#plt.legend()
#plt.savefig("Balance.png")
#plt.show






