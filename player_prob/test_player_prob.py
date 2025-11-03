import numpy as np

def card(i, decks, cards):
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

def read_value(c1, c2, cards, decks, i):
  from player_prob import probp
  sip, sep, eip, nip, tep, elp, twp, thp, fp, ffp, sxp, sp, ep, np, tp, typ, bustp = probp(c1, c2, cards, decks, i)

  print(f"{sip:.3f}", f"{sep:.3f}", f"{eip:.3f}", f"{nip:.3f}", f"{tep:.3f}", f"{elp:.3f}", f"{twp:.3f}", f"{thp:.3f}", f"{fp:.3f}", f"{ffp:.3f}", f"{sxp:.3f}", f"{sp:.3f}", f"{ep:.3f}", f"{np:.3f}", f"{tp:.3f}", f"{typ:.3f}", f"{bustp:.3f}", sip+sep+eip+nip+tep+elp+twp+thp+fp+ffp+sxp+sp+ep+np+tp+typ+bustp)


decks = 1

cards = np.empty(10)
for j in range (10):
  if j == 8:
      cards[j] = decks*16
  else:
      cards[j] = decks*4

i = 2

for k in range (10):
  cards[k] -= 1
  c2 = k + 2
  for j in range(10):
    cards[j] -= 1
    c1 = j + 2
    value = read_value(c1, c2, cards, decks, i)
    print(k+2, j+2)
    cards[j] += 1
  cards[k] += 1
