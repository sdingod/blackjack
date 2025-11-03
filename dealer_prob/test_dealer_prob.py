import numpy as np

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
  
def read_value(d1, cards, decks, i):
  from dealer_prob import probd
  sp, ep, np, tp, typ, bustp = probd(d1, cards, decks, i)

  print(f"{sp:.3f}", f"{ep:.3f}", f"{np:.3f}", f"{tp:.3f}", f"{typ:.3f}", f"{bustp:.3f}", sp+ep+np+tp+typ+bustp)
decks = 1

cards = np.empty(10)
for j in range (10):
  if j == 8:
      cards[j] = decks*16
  else:
      cards[j] = decks*4

i = 1

for j in range(10):
  cards[j] -= 1
  d1 = j + 2
  value = read_value(d1, cards, decks, i)
  print(j+2)
  i += 1