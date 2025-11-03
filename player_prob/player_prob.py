def probp(c1, c2, cards, decks, i): #Idk how to do this with a recursive function
  sip = sep = eip = nip = tep = elp = twp = thp = fp = ffp = sxp = sp = ep = np = tp = typ = bustp = 0.
  c2c = c2

  if (c1 == c2 == 11):
    c2c = 1

  for ja in range(10):
    c = c1 + c2c

    if (c1 == 11 or c2 == 11 or c > 11):
      acec = 1
    else:
      acec = 0
    
    c3 = ja + 2

    if (c3 == 11 and acec == 1):
      c3 = 1

    c += c3

    prob = cards[ja]/(decks*52-i)

    if (c >= 22):
      bustp += prob
    elif (c == 21):
      typ += prob
    elif (c == 20):
      tp += prob
    elif (c == 19):
      np += prob
    elif (c == 18):
      ep += prob
    elif (c == 17):
      sp += prob
    elif (c == 16):
      sxp += prob
    elif (c == 15):
      ffp += prob
    elif (c == 14):
      fp += prob
    elif (c == 13):
      thp += prob
    elif (c == 12):
      twp += prob
    elif (c == 11):
      elp += prob
    elif (c == 10):
      tep += prob
    elif (c == 9):
      nip += prob
    elif (c == 8):
      eip += prob
    elif (c == 7):
      sep += prob
    elif (c == 6):
      sip += prob
  
  return sip, sep, eip, nip, tep, elp, twp, thp, fp, ffp, sxp, sp, ep, np, tp, typ, bustp

