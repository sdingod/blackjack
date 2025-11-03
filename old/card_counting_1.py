def leggi_valore(filepath, riga_x, colonna_y, TC):
  if (filepath == "S2_1.txt" and TC < -2 and riga_x == 13 and colonna_y == 3):
    return "H"
  elif (filepath == "S2_1.txt" and TC < -1 and ((riga_x == 13 and colonna_y == 2) or (riga_x == 16 and colonna_y == 9))):
    return "H"
  elif (filepath == "S2_1.txt" and TC < 0 and ((riga_x == 12 and colonna_y == 4) or (riga_x == 15 and colonna_y == 10))):
    return "H"
  elif (filepath == "S2_1.txt" and TC > 0 and riga_x == 16 and colonna_y == 10):
    return "S"
  elif (filepath == "S2_1.txt" and TC > 1 and ((riga_x == 11 and colonna_y == 11) or (riga_x == 9 and colonna_y == 2))):
    return "D"
  elif (filepath == "S3_1.txt" and TC > 1 and riga_x == 6 and colonna_y == 2):
    return "D"  
  elif (filepath == "S3_1.txt" and TC > 1 and ((riga_x == 8 and colonna_y == 5) or (riga_x == 8 and colonna_y == 6))):
    return "G"
  elif (filepath == "S2_1.txt" and TC > 2 and ((riga_x == 15 and colonna_y == 9) or (riga_x == 15 and colonna_y == 11))):
    return "U"
  elif (filepath == "S2_1.txt" and TC > 2 and riga_x == 8 and colonna_y == 6):
    return "D"
  elif (filepath == "S2_1.txt" and TC > 2 and riga_x == 12 and colonna_y == 3):
    return "S"
  elif (filepath == "S2_1.txt" and TC > 3 and riga_x == 12 and colonna_y == 2):
    return "S"
  elif (filepath == "S2_1.txt" and TC > 3 and riga_x == 9 and colonna_y == 7):
    return "D"
  elif (filepath == "S3_1.txt" and TC > 3 and riga_x == 8 and colonna_y == 4):
    return "G"
  elif (filepath == "S2_1.txt" and TC > 4 and riga_x == 16 and colonna_y == 6):
    return "U"
  elif (filepath == "S2_1.txt" and TC > 4 and ((riga_x == 16 and colonna_y == 9) or (riga_x == 15 and colonna_y == 10))):
    return "S"
  elif (filepath == "S2_1.txt" and TC > 4 and ((riga_x == 10 and colonna_y == 10) or (riga_x == 10 and colonna_y == 11))):
    return "D"
  elif (filepath == "S1_1.txt" and TC > 4 and riga_x == 10 and colonna_y == 6):
    return "Y"
  elif (filepath == "S1_1.txt" and TC > 5 and riga_x == 10 and colonna_y == 5):
    return "Y"
  elif (filepath == "S1_1.txt" and TC > 6 and riga_x == 10 and colonna_y == 4):
    return "Y"
  else:
    with open(filepath, 'r') as file:
        for i, linea in enumerate(file):
            if i == riga_x - 1:  # -1 perché le righe partono da 0
                valori = linea.strip().split()
                if colonna_y - 1 < len(valori):  # Controlla se la colonna esiste
                    return valori[colonna_y - 1]
                else:
                    return None
  return None

def carta(commento, RC, i, decks):
  i += 1
  while True:
    c = input(commento)
    try:
      c_int = int(c)
      if c_int in [2, 3, 4, 5, 6]:
        RC += 1.0
        break
      elif c_int in [7, 8, 9]:
        # RC rimane invariato
        break
      elif c_int in [10, 11]:
        RC -= 1.0
        break
      else:
        print("valore errato, reinserire")
    except ValueError:
      if c == "n":
        i -= 1
        break
      elif c == "stop":
        break
      elif c == "bj":
        break
      else:
        print("Inserisci un numero valido!")
  TC = RC / (decks - i/52)

  return c, RC, i, TC


#rules: 10,J,Q,K = 10
#       A = 11
#       carte date con double vanno in quelle addizionali

#number of decks
deck = input ("Number of decks: ")
decks = float(deck)
#true count
RC = 0.
i = 0.

while 1 == 1:
  #carte iniziali
  c1, RC, i, TC = carta("Carta 1: ", RC, i, decks)
  d, RC, i, TC = carta("Dealer: ", RC, i, decks)
  if (int(d) == 11 and TC >3):
    print("Take insurance")
  c2, RC, i, TC = carta("Carta 2: ", RC, i, decks)

  c = 0


  #scenario 1

  if (int(c1) != int(c2) and int(c1) != 11 and int(c2) != 11):
    while 1 == 1:
      s = int(c1) + int(c2)
      valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
      if (valore == "U" or ((TC < 4 and TC > -1) and s == 16 and int(d) == 9) or (TC < 0 and s == 16 and int(d) == 10) or (s == 16 and int(d) == 11) or ((TC < 4 and TC > 0) and s == 15 and int(d) == 10)):
        print("\033[91mSurrender\033[0m")
        break   
      elif (valore == "H"):
        print("\033[92mHit\033[0m")
      else:
        if (valore == "S"):
          print ("\033[91mStand\033[0m")
          break
        else:
          if (valore == "D"):
            print("\033[94mDouble\033[0m")
            break
          else:
            print("\033[95mError\033[0m")
            break

      while 1 == 1:
        c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
        if c == "bj":
          break

        if (s > 10 and int(c) == 11):
          c = 1

        if (s+int(c) > 21):
          print ("\033[93mBust\033[0m")
          break

        if (int(c) != 11):
          s += int(c)
          valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
          if (valore == "H"):
            print("\033[92mHit\033[0m")
          else:
            if (valore == "S"):
              print ("\033[91mStand\033[0m")
              break
            else:
              if (valore == "D"):
                print("\033[94mDouble\033[0m")
                break
              else:
                print("\033[95mError\033[0m")
                break
            
        if (int(c) == 11):
          valore = leggi_valore("S3_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
          if (valore == "H"):
            print("\033[92mHit\033[0m")
          else:
            if (valore == "S"):
              print ("\033[91mStand\033[0m")
              break
            else:
              if (valore == "D"):
                print("\033[94mDouble\033[0m")
                break
              else:
                if (valore == "G"):
                  print("\033[94mDouble, otherwise stand\033[0m")
                  break
                else:
                  print("\033[95mError\033[0m")
                  break

          while 1 == 1:
            c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
            if c == "n":
              break

            if (int(c) == 11):
              c = 1
            s += int(c)

            if ((s+1) > 21):
              print ("\033[93mBust\033[0m")
              break
            
            if (s < 11):
              valore = leggi_valore("S3_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
              if (valore == "H"):
                print("\033[92mHit\033[0m")
              else:
                if (valore == "S"):
                  print ("\033[91mStand\033[0m")
                  break
                else:
                  if (valore == "D"):
                    print("\033[94mDouble\033[0m")
                    break
                  else:
                    if (valore == "G"):
                      print("\033[94mDouble, otherwise stand\033[0m")
                      break
                    else:
                      print("\033[95mError\033[0m")
                      break

            if (s > 10):
              s += 1
              while 1 == 1:
                valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
                if (valore == "H"):
                  print("\033[92mHit\033[0m")
                else:
                  if (valore == "S"):
                    print ("\033[91mStand\033[0m")
                    break
                  else:
                    if (valore == "D"):
                      print("\033[94mDouble\033[0m")
                      break
                    else:
                      print("\033[95mError\033[0m")
                      break
                
                c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
                if c == "n":
                  break
                  
                s += int(c)
                if (s > 21):
                  print ("\033[93mBust\033[0m")
                  break
              break
          break
      break      


  #scenario 2 - aces

  if (int(c1) != int(c2) and (int(c1) == 11 or int(c2) == 11)):
    while 1 == 1:
      if (int(c1) == 11):
        s = int(c2)       
      else:
        s = int(c1)
      valore = leggi_valore("S3_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
      if (valore == "H"):
        print("\033[92mHit\033[0m")
      else:
        if (valore == "S"):
          print ("\033[91mStand\033[0m")
          break
        else:
          if (valore == "D"):
            print("\033[94mDouble\033[0m")
            break
          else:
            if (valore == "G"):
              print("\033[94mDouble, otherwise stand\033[0m")
              break
            else:
              print("\033[95mError\033[0m")
              break

      while 1 == 1:
        c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
        if c == "bj":
          break
          
        if (int(c) == 11):
          c = 1
        s += int(c)
        
        if ((s + 1) > 21):
          print("\033[93mBust\033[0m")
          break

        if (s < 11):
          valore = leggi_valore("S3_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
          if (valore == "H"):
            print("\033[92mHit\033[0m")
          else:
            if (valore == "S"):
              print ("\033[91mStand\033[0m")
              break
            else:
              if (valore == "D"):
                print("\033[94mDouble\033[0m")
                break
              else:
                if (valore == "G"):
                  print("\033[94mDouble, otherwise stand\033[0m")
                  break
                else:
                  print("\033[95mError\033[0m")
                  break

        if (s > 10):
          s += 1
          while 1 == 1:
            valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
            if (valore == "H"):
              print("\033[92mHit\033[0m")
            else:
              if (valore == "S"):
                print ("\033[91mStand\033[0m")
                break
              else:
                if (valore == "D"):
                  print("\033[94mDouble\033[0m")
                  break
                else:
                  print("\033[95mError\033[0m")
                  break
            
            c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
            if c == "n":
              break
              
            s += int(c)
            if (s > 21):
              print ("\033[93mBust\033[0m")
              break  
          break
      break


  #scenario 3 - split

  if (int(c1) == int(c2)):
    while 1 == 1:
      valore = leggi_valore("S1_1.txt", riga_x = int(c1), colonna_y = int(d), TC = TC)
      if (valore == "Y"):
        print("\033[96mSplit\033[0m")
        for x in range (0, 2):
          print ("giocata: ", x+1)
          c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
          if c == "bj":
            break   

          a = c         

          #scenario 1

          if (int(c1) != 11 and int(c) != 11):
            while 1 == 1:
              s = int(c1) + int(c)
              valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
              if (valore == "H"):
                print("\033[92mHit\033[0m")
              else:
                if (valore == "S"):
                  print ("\033[91mStand\033[0m")
                  break
                else:
                  if (valore == "D"):
                    print("\033[94mDouble\033[0m")
                    break
                  else:
                    print("\033[95mError\033[0m")
                    break

              while 1 == 1:
                c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
                if c == "n":
                  break
              
                if (s > 10 and int(c) == 11):
                  c = 1

                if (s+int(c) > 21):
                  print ("\033[93mBust\033[0m")
                  break

                if (int(c) != 11):
                  s += int(c)
                  valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
                  if (valore == "H"):
                    print("\033[92mHit\033[0m")
                  else:
                    if (valore == "S"):
                      print ("\033[91mStand\033[0m")
                      break
                    else:
                      if (valore == "D"):
                        print("\033[94mDouble\033[0m")
                        break
                      else:
                        print("\033[95mError\033[0m")
                        break
                    
                if (int(c) == 11):
                  valore = leggi_valore("S3_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
                  if (valore == "H"):
                    print("\033[92mHit\033[0m")
                  else:
                    if (valore == "S"):
                      print ("\033[91mStand\033[0m")
                      break
                    else:
                      if (valore == "D"):
                        print("\033[94mDouble\033[0m")
                        break
                      else:
                        if (valore == "G"):
                          print("\033[94mDouble, otherwise stand\033[0m")
                          break
                        else:
                          print("\033[95mError\033[0m")
                          break

                  while 1 == 1:
                    c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
                    if c == "n":
                      break
              
                    if (int(c) == 11):
                      c = 1
                    s += int(c)

                    if ((s+1) > 21):
                      print ("\033[93mBust\033[0m")
                      break
                    
                    if (s < 11):
                      valore = leggi_valore("S3_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
                      if (valore == "H"):
                        print("\033[92mHit\033[0m")
                      else:
                        if (valore == "S"):
                          print ("\033[91mStand\033[0m")
                          break
                        else:
                          if (valore == "D"):
                            print("\033[94mDouble\033[0m")
                            break
                          else:
                            if (valore == "G"):
                              print("\033[94mDouble, otherwise stand\033[0m")
                              break
                            else:
                              print("\033[95mError\033[0m")
                              break

                    if (s > 10):
                      s += 1
                      while 1 == 1:
                        valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
                        if (valore == "H"):
                          print("\033[92mHit\033[0m")
                        else:
                          if (valore == "S"):
                            print ("\033[91mStand\033[0m")
                            break
                          else:
                            if (valore == "D"):
                              print("\033[94mDouble\033[0m")
                              break
                            else:
                              print("\033[95mError\033[0m")
                              break
                        
                        c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
                        if c == "n":
                          break
              
                        s += int(c)
                        if (s > 21):
                          print ("\033[93mBust\033[0m")
                          break
                      break
                  break
              break
        
          c = a
          # scenario 2     

          if (int(c1) != int(c) and (int(c1) == 11 or int(c) == 11)):
            while 1 == 1:
              if (int(c1) == 11):
                s = int(c)       
              else:
                s = int(c1)
              valore = leggi_valore("S3_1.txt", riga_x = int(c1), colonna_y = int(d), TC = TC)
              if (valore == "H"):
                print("\033[92mHit\033[0m")
              else:
                if (valore == "S"):
                  print ("\033[91mStand\033[0m")
                  break
                else:
                  if (valore == "D"):
                    print("\033[94mDouble\033[0m")
                    break
                  else:
                    if (valore == "G"):
                      print("\033[94mDouble, otherwise stand\033[0m")
                      break
                    else:
                      print("\033[95mError\033[0m")
                      break

              while 1 == 1:
                c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
                if c == "n":
                  break
            
                if (int(c) == 11):
                  c = 1
                s += int(c)
                
                if ((s + 1) > 21):
                  print("\033[93mBust\033[0m")
                  break

                if (s < 11):
                  valore = leggi_valore("S3_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
                  if (valore == "H"):
                    print("\033[92mHit\033[0m")
                  else:
                    if (valore == "S"):
                      print ("\033[91mStand\033[0m")
                      break
                    else:
                      if (valore == "D"):
                        print("\033[94mDouble\033[0m")
                        break
                      else:
                        if (valore == "G"):
                          print("\033[94mDouble, otherwise stand\033[0m")
                          break
                        else:
                          print("\033[95mError\033[0m")
                          break

                if (s > 10):
                  s += 1
                  while 1 == 1:
                    valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
                    if (valore == "H"):
                      print("\033[92mHit\033[0m")
                    else:
                      if (valore == "S"):
                        print ("\033[91mStand\033[0m")
                        break
                      else:
                        if (valore == "D"):
                          print("\033[94mDouble\033[0m")
                          break
                        else:
                          print("\033[95mError\033[0m")
                          break
                    
                    c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
                    if c == "n":
                      break
            
                    s += int(c)
                    if (s > 21):
                      print ("\033[93mBust\033[0m")
                      break  
                  break
              break  
      else:
        if (valore == "N"):
          s = int(c1) + int(c2)
          valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
          if (valore == "H"):
            print("\033[92mHit\033[0m")
          else:
            if (valore == "S"):
              print ("\033[91mStand\033[0m")
              break
            else:
              if (valore == "D"):
                print("\033[94mDouble\033[0m")
                break
              else:
                print("\033[95mError\033[0m")
                break

          while 1 == 1:
            c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
            if c == "bj":
              break
              
            if (s > 10 and int(c) == 11):
              c = 1

            if (s+int(c) > 21):
              print ("\033[93mBust\033[0m")
              break

            if (int(c) != 11):
              s += int(c)
              valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
              if (valore == "H"):
                print("\033[92mHit\033[0m")
              else:
                if (valore == "S"):
                  print ("\033[91mStand\033[0m")
                  break
                else:
                  if (valore == "D"):
                    print("\033[94mDouble\033[0m")
                    break
                  else:
                    print("\033[95mError\033[0m")
                    break
                
            if (int(c) == 11):
              valore = leggi_valore("S3_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
              if (valore == "H"):
                print("\033[92mHit\033[0m")
              else:
                if (valore == "S"):
                  print ("\033[91mStand\033[0m")
                  break
                else:
                  if (valore == "D"):
                    print("\033[94mDouble\033[0m")
                    break
                  else:
                    if (valore == "G"):
                      print("\033[94mDouble, otherwise stand\033[0m")
                      break
                    else:
                      print("\033[95mError\033[0m")
                      break

              while 1 == 1:
                c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
                if c == "n":
                  break
              
                if (int(c) == 11):
                  c = 1
                s += int(c)

                if ((s+1) > 21):
                  print ("\033[93mBust\033[0m")
                  break
                
                if (s < 11):
                  valore = leggi_valore("S3_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
                  if (valore == "H"):
                    print("\033[92mHit\033[0m")
                  else:
                    if (valore == "S"):
                      print ("\033[91mStand\033[0m")
                      break
                    else:
                      if (valore == "D"):
                        print("\033[94mDouble\033[0m")
                        break
                      else:
                        if (valore == "G"):
                          print("\033[94mDouble, otherwise stand\033[0m")
                          break
                        else:
                          print("\033[95mError\033[0m")
                          break

                if (s > 10):
                  s += 1
                  while 1 == 1:
                    valore = leggi_valore("S2_1.txt", riga_x = s, colonna_y = int(d), TC = TC)
                    if (valore == "H"):
                      print("\033[92mHit\033[0m")
                    else:
                      if (valore == "S"):
                        print ("\033[91mStand\033[0m")
                        break
                      else:
                        if (valore == "D"):
                          print("\033[94mDouble\033[0m")
                          break
                        else:
                          print("\033[95mError\033[0m")
                          break
                    
                    c, RC, i, TC = carta("Nuova Carta: ", RC, i, decks)
                    if c == "n":
                      break
              
                    s += int(c)
                    if (s > 21):
                      print ("\033[93mBust\033[0m")
                      break
                  break
              break
        else:
          print ("\033[95mError\033[0m")
          break
      break

  while 1 == 1:
    c, RC, i, TC = carta("Carte addizionali: ", RC, i, decks)
    if (c == "n" or c == "stop"):
      break
  
  if c == "stop":
    break
  
  print ("True count: ", TC)
  print ("---------- NUOVA GIOCATA ----------")