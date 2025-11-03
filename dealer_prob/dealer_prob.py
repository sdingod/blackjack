def probd(d1, cards, decks, i): #Idk how to do this with a recursive function
  sp = 0.
  ep = 0.
  np = 0.
  tp = 0.
  typ = 0.
  bustp = 0.
  cardf = cards.copy()
  for ja in range (10): #worst case d = 4
    cards = cardf.copy()
    d = d1

    if d1 == 11:
      acec = 1
    else:
      acec = 0

    if cards[ja] == 0:
      continue
    else:
      d2 = ja + 2

      if (d2 == 11 and acec == 1):
        d2 = 1

      if (d1 == 11 or d2 == 11):
        acec = 1
      else:
        acec = 0
      
      d = d1 + d2

      prob = cards[ja]/(decks*52-i)
      if d > 21:
        bustp += prob
      elif d == 21:
        typ += prob
      elif d == 20:
        tp += prob
      elif d == 19:
        np += prob
      elif d == 18:
        ep += prob
      elif d == 17:
        sp += prob
      else:
        cards[ja] -= 1

        for jb in range (10): #worst case d = 6

          d = d1 + d2
          if (d1 == 11 or d2 == 11 or d >= 11):
            acec = 1
          else:
            acec = 0

          if cards[jb] == 0:
            continue
          else:
            d3 = jb + 2

            if (d3 == 11 and acec == 1):
              d3 = 1
            
            d += d3

            prob = (cards[ja]+1)*cards[jb]/((decks*52-i)*(decks*52-i-1))

            if d > 21:
              bustp += prob
            elif d == 21:
              typ += prob
            elif d == 20:
              tp += prob
            elif d == 19:
              np += prob
            elif d == 18:
              ep += prob
            elif d == 17:
              sp += prob
            else:
              cards[jb] -= 1

              for jc in range (10): #worst case d = 8
                d = d1 + d2 + d3
                if (d1 == 11 or d2 == 11 or d3 == 11 or d >= 11):
                  acec = 1
                else:
                  acec = 0

                if cards[jc] == 0:
                  continue
                else:
                  d4 = jc + 2

                  if (d4 == 11 and acec == 1):
                    d4 = 1
                  
                  d += d4

                  if (ja == jb):
                    prob = (cards[ja]+2)*(cards[jb]+1)*cards[jc]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2))
                  else:
                    prob = (cards[ja]+1)*(cards[jb]+1)*cards[jc]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2))

                  if d > 21:
                    bustp += prob
                  elif d == 21:
                    typ += prob
                  elif d == 20:
                    tp += prob
                  elif d == 19:
                    np += prob
                  elif d == 18:
                    ep += prob
                  elif d == 17:
                    sp += prob
                  else:
                    cards[jc] -= 1

                    for jd in range (10): #worst case d = 10
                      d = d1 + d2 + d3 + d4
                      if (d1 == 11 or d2 == 11 or d3 == 11 or d4 == 11 or d >= 11):
                        acec = 1
                      else:
                        acec = 0

                      if cards[jd] == 0:
                        continue
                      else:
                        d5 = jd + 2

                        if (d5 == 11 and acec == 1):
                          d5 = 1
                        
                        d += d5

                        if (ja == jb == jc):
                          prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+1)*cards[jd]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3))
                        elif (ja == jb != jc):
                          prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*cards[jd]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3))
                        elif (ja == jc != jb):
                          prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*cards[jd]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3))
                        elif (jb == jc != ja):
                          prob = (cards[ja]+1)*(cards[jb]+2)*(cards[jc]+1)*cards[jd]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3))
                        else:
                          prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+1)*cards[jd]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3))

                        if d > 21:
                          bustp += prob
                        elif d == 21:
                          typ += prob
                        elif d == 20:
                          tp += prob
                        elif d == 19:
                          np += prob
                        elif d == 18:
                          ep += prob
                        elif d == 17:
                          sp += prob
                        else:
                          cards[jd] -= 1

                          for je in range (10): #worst case d = 12
                            d = d1 + d2 + d3 + d4 + d5
                            if (d1 == 11 or d2 == 11 or d3 == 11 or d4 == 11 or d5 == 11 or d >= 11):
                              acec = 1
                            else:
                              acec = 0

                            if cards[je] == 0:
                              continue
                            else:
                              d6 = je + 2

                              if (d6 == 11 and acec == 1):
                                d6 = 1
                              
                              d += d6

                              if (ja == jb == jc == jd):
                                prob = (cards[ja]+4)*(cards[jb]+3)*(cards[jc]+2)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (ja == jb == jc != jd):
                                prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (ja == jb == jd != jc):
                                prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (ja == jc == jd != jb):
                                prob = (cards[ja]+3)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (jb == jc == jd != ja):
                                prob = (cards[ja]+1)*(cards[jb]+3)*(cards[jc]+2)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (ja == jb != jc != jd):
                                prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (ja == jb != jc == jd):
                                prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (ja == jc != jb != jd):
                                prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (ja == jc != jb == jd):
                                prob = (cards[ja]+2)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (ja == jd != jb != jc):
                                prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (ja == jd != jb == jc):
                                prob = (cards[ja]+2)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (jb == jc != ja != jd):
                                prob = (cards[ja]+1)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (jb == jd != ja != jc):
                                prob = (cards[ja]+1)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              elif (jc == jd != ja != jb):
                                prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))
                              else:
                                prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*cards[je]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4))

                              if d > 21:
                                bustp += prob
                              elif d == 21:
                                typ += prob
                              elif d == 20:
                                tp += prob
                              elif d == 19:
                                np += prob
                              elif d == 18:
                                ep += prob
                              elif d == 17:
                                sp += prob
                              else:
                                cards[je] -= 1

                                for jf in range (10): #worst case d = 13
                                  d = d1 + d2 + d3 + d4 + d5 + d6
                                  if (d1 == 11 or d2 == 11 or d3 == 11 or d4 == 11 or d5 == 11 or d6 == 11 or d >= 11):
                                    acec = 1
                                  else:
                                    acec = 0

                                  if cards[jf] == 0:
                                    continue
                                  else:
                                    d7 = jf + 2

                                    if (d7 == 11 and acec == 1):
                                      d7 = 1
                                    
                                    d += d7

                                    if (ja == jb == jc == jd == je):
                                      prob = (cards[ja]+5)*(cards[jb]+4)*(cards[jc]+3)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (jb == jc == jd == je != ja):
                                      prob = (cards[ja]+1)*(cards[jb]+4)*(cards[jc]+3)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jb == jc == jd != ja != je) and (jb != je)):
                                      prob = (cards[ja]+1)*(cards[jb]+3)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jb == jc == je != ja != jd) and (jb != jd)):
                                      prob = (cards[ja]+1)*(cards[jb]+3)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jb == jd == je != ja != jc) and (jb != jc)):
                                      prob = (cards[ja]+1)*(cards[jb]+3)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jc == jd == je != ja != jb) and (jc != jb)):
                                      prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+3)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jc != jb == je != ja) and (jc == jd != ja)):
                                      prob = (cards[ja]+1)*(cards[jb]+2)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jc != jb == jd != ja) and (jc == je != ja)):
                                      prob = (cards[ja]+1)*(cards[jb]+2)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jd != jb == jc != ja) and (jd == je != ja)):
                                      prob = (cards[ja]+1)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja != jc) and (ja != je) and (jb != je) and (ja != jb != jc == jd != je)):
                                      prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja != jc) and (ja != jd) and (jb != jd) and (ja != jb != jc == je != jd)):
                                      prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja != jc) and (ja != jd) and (jb != jd) and (ja != jb != jc != jd == je)):
                                      prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja != jb) and (ja != jc) and (ja != jd) and (jb != jc) and (jb != jd) and (jb == je) and (jc != jd)):
                                      prob = (cards[ja]+1)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja != jb) and (ja != jc) and (ja != je) and (jb != jc) and (jb != je) and (jb == jd) and (jc != jd)):
                                      prob = (cards[ja]+1)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja != jb) and (ja != jd) and (ja != je) and (jb == jc) and (jb != jd) and (jb != je) and (jd != je)):
                                      prob = (cards[ja]+1)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (ja == jb != jc == jd == je):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+3)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jc != ja == jb != je) and (jc == jd != je)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jc != ja == jb != jd) and (jc == je != jd)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jd != ja == jb != jc) and (jd == je != jc)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jd != ja == jc != jb) and (jd == je != jb)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja == jb) and (ja != jc) and (ja != jd) and (ja != je) and (jc != jd) and (jc != je) and (jd != je)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja != jb) and (ja == jc) and (ja != jd) and (ja != je) and (jb != jd) and (jb != je) and (jd != je)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja != jb) and (ja != jc) and (ja != jd) and (ja == je) and (jb != jc) and (jb != jd) and (jc != jd)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja != jb) and (ja != jc) and (ja == jd) and (ja != je) and (jb != jc) and (jb != je) and (jc != je)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja == jc != jd != jb == je) and (ja != jb)):
                                      prob = (cards[ja]+2)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja == jc != je != jb == jd) and (ja != jb)):
                                      prob = (cards[ja]+2)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (ja == jc != jd == jb == je):
                                      prob = (cards[ja]+2)*(cards[jb]+3)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja == jd != je != jb == jc) and (ja != jb)):
                                      prob = (cards[ja]+2)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (ja == jd != jc == jb == je):
                                      prob = (cards[ja]+2)*(cards[jb]+3)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (ja == je != jc == jb == jd):
                                      prob = (cards[ja]+2)*(cards[jb]+3)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja == je != jb != jd == jc) and (ja != jd)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja == jd != jb != je == jc) and (ja != je)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jb != ja == jc == je != jd) and (jb != jd)):
                                      prob = (cards[ja]+3)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jb != ja == jc == jd != je) and (jb != je)):
                                      prob = (cards[ja]+3)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jc != ja == jb == je != jd) and (jc != jd)):
                                      prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jc != ja == jb == jd != je) and (jc != je)):
                                      prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jd != ja == jc == jb != je) and (jd != je)):
                                      prob = (cards[ja]+3)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja == jd != jc != je == jb) and (ja != jb)):
                                      prob = (cards[ja]+2)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja == je != jc != jb == jd) and (ja != jb)):
                                      prob = (cards[ja]+2)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((ja == je != jd != jb == jc) and (ja != jc)):
                                      prob = (cards[ja]+2)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (ja == jd == je != jb == jc):
                                      prob = (cards[ja]+3)*(cards[jb]+1)*(cards[jc]+2)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif ((jb != ja == jd == je != jc) and (jb != jc)):
                                      prob = (cards[ja]+3)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (jb == ja == jd == jc != je):
                                      prob = (cards[ja]+3)*(cards[jb]+4)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (je == ja == jd == jc != jb):
                                      prob = (cards[ja]+3)*(cards[jb]+1)*(cards[jc]+4)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (je == ja == jc != jb == jd):
                                      prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (jd == ja == jc != jb == je):
                                      prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (jb == ja == jc != jd == je):
                                      prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (jd == ja == jb != jc == je):
                                      prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (jb == ja == je != jc == jd):
                                      prob = (cards[ja]+3)*(cards[jb]+2)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (jb == ja == je == jd != jc):
                                      prob = (cards[ja]+4)*(cards[jb]+3)*(cards[jc]+1)*(cards[jd]+2)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    elif (jb == ja == je == jc != jd):
                                      prob = (cards[ja]+4)*(cards[jb]+3)*(cards[jc]+2)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                    else:
                                      prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*cards[jf]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5))
                                      print("a")

                                    if d > 21:
                                      bustp += prob
                                    elif d == 21:
                                      typ += prob
                                    elif d == 20:
                                      tp += prob
                                    elif d == 19:
                                      np += prob
                                    elif d == 18:
                                      ep += prob
                                    elif d == 17:
                                      sp += prob
                                    else:
                                      cards[jf] -= 1

                                      for jg in range (10): #worst case d = 14
                                        d = d1 + d2 + d3 + d4 + d5 + d6 + d7
                                        if (d1 == 11 or d2 == 11 or d3 == 11 or d4 == 11 or d5 == 11 or d6 == 11 or d7 == 11 or d >= 11):
                                          acec = 1
                                        else:
                                          acec = 0

                                        if cards[jg] == 0:
                                          continue
                                        else:
                                          d8 = jg + 2

                                          if (d8 == 11 and acec == 1):
                                            d8 = 1
                                          
                                          d += d8

                                          #Don't want to put ~100 conditions to justify 10 e**(-6) error on probability normalization
                                          
                                          prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*(cards[jf]+1)*cards[jg]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5)*(decks*52-i-6))
                                          if d > 21:
                                            bustp += prob
                                          elif d == 21:
                                            typ += prob
                                          elif d == 20:
                                            tp += prob
                                          elif d == 19:
                                            np += prob
                                          elif d == 18:
                                            ep += prob
                                          elif d == 17:
                                            sp += prob
                                          else:
                                            cards[jg] -= 1

                                            for jh in range (10): #worst case d = 15
                                              d = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8
                                              if (d1 == 11 or d2 == 11 or d3 == 11 or d4 == 11 or d5 == 11 or d6 == 11 or d7 == 11 or d8 == 11 or d >= 11):
                                                acec = 1
                                              else:
                                                acec = 0

                                              if cards[jh] == 0:
                                                continue
                                              else:
                                                d9 = jh + 2

                                                if (d9 == 11 and acec == 1):
                                                  d9 = 1
                                                
                                                d += d9

                                                #Don't want to put ~100 conditions to justify 10 e**(-6) error on probability normalization
                                                
                                                prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*(cards[jf]+1)*(cards[jg]+1)*cards[jh]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5)*(decks*52-i-6)*(decks*52-i-7))
                                                if d > 21:
                                                  bustp += prob
                                                elif d == 21:
                                                  typ += prob
                                                elif d == 20:
                                                  tp += prob
                                                elif d == 19:
                                                  np += prob
                                                elif d == 18:
                                                  ep += prob
                                                elif d == 17:
                                                  sp += prob
                                                else:
                                                  cards[jh] -= 1

                                                  for ji in range (10): #worst case d = 16
                                                    d = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
                                                    if (d1 == 11 or d2 == 11 or d3 == 11 or d4 == 11 or d5 == 11 or d6 == 11 or d7 == 11 or d8 == 11 or d9 == 11 or d >= 11):
                                                      acec = 1
                                                    else:
                                                      acec = 0

                                                    if cards[ji] == 0:
                                                      continue
                                                    else:
                                                      d10 = ji + 2

                                                      if (d10 == 11 and acec == 1):
                                                        d10 = 1
                                                      
                                                      d += d10

                                                      #Don't want to put ~100 conditions to justify 10 e**(-6) error on probability normalization
                                                      prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*(cards[jf]+1)*(cards[jg]+1)*(cards[jh]+1)*cards[ji]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5)*(decks*52-i-6)*(decks*52-i-7)*(decks*52-i-8))
                                                      
                                                      if d > 21:
                                                        bustp += prob
                                                      elif d == 21:
                                                        typ += prob
                                                      elif d == 20:
                                                        tp += prob
                                                      elif d == 19:
                                                        np += prob
                                                      elif d == 18:
                                                        ep += prob
                                                      elif d == 17:
                                                        sp += prob
                                                      else:
                                                        cards[ji] -= 1

                                                        for jj in range (10): #worst case d = 17
                                                          d = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10
                                                          if (d1 == 11 or d2 == 11 or d3 == 11 or d4 == 11 or d5 == 11 or d6 == 11 or d7 == 11 or d8 == 11 or d9 == 11 or d10 == 11 or d >= 11):
                                                            acec = 1
                                                          else:
                                                            acec = 0

                                                          if cards[jj] == 0:
                                                            continue
                                                          else:
                                                            d11 = jj + 2

                                                            if (d11 == 11 and acec == 1):
                                                              d11 = 1
                                                            
                                                            d += d11

                                                            #Don't want to put ~100 conditions to justify 10 e**(-6) error on probability normalization
                                                            prob = (cards[ja]+1)*(cards[jb]+1)*(cards[jc]+1)*(cards[jd]+1)*(cards[je]+1)*(cards[jf]+1)*(cards[jg]+1)*(cards[jh]+1)*(cards[ji]+1)*cards[jj]/((decks*52-i)*(decks*52-i-1)*(decks*52-i-2)*(decks*52-i-3)*(decks*52-i-4)*(decks*52-i-5)*(decks*52-i-6)*(decks*52-i-7)*(decks*52-i-8)*(decks*52-i-9))
                                                            
                                                            if d > 21:
                                                              bustp += prob
                                                            elif d == 21:
                                                              typ += prob
                                                            elif d == 20:
                                                              tp += prob
                                                            elif d == 19:
                                                              np += prob
                                                            elif d == 18:
                                                              ep += prob
                                                            elif d == 17:
                                                              sp += prob
                                                        cards[ji] += 1
                                                  cards[jh] += 1
                                            cards[jg] += 1
                                      cards[jf] += 1
                                cards[je] += 1
                          cards[jd] += 1
                    cards[jc] += 1
              cards[jb] += 1
        cards[ja] += 1

  cards = cardf.copy()
  return sp, ep, np, tp, typ, bustp