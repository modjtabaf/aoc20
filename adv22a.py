
if 0:
  Player1 = [
    9,
    2,
    6,
    3,
    1]

  Player2 = [
    5,
    8,
    4,
    7,
    10]
    
else:
  Player1 = [
    21,
    48,
    44,
    31,
    29,
    5,
    23,
    11,
    12,
    27,
    49,
    22,
    18,
    7,
    15,
    20,
    2,
    45,
    14,
    17,
    40,
    35,
    6,
    24,
    41]

  Player2 = [
    47,
    1,
    10,
    16,
    28,
    37,
    8,
    26,
    46,
    25,
    3,
    9,
    34,
    50,
    32,
    36,
    43,
    4,
    42,
    33,
    19,
    13,
    38,
    39,
    30]

def game(deck1, deck2):
  while True:
    if len(deck1) == 0:
      winner = 2
      break
    elif len(deck2) == 0:
      winner = 1
      break

    card1 = deck1[0]; deck1 = deck1[1:]
    card2 = deck2[0]; deck2 = deck2[1:]

    if card1 > card2:
      winner = 1
      deck1 += [card1, card2]
    else:
      winner = 2
      deck2 += [card2, card1]

  return winner, deck1, deck2

winner, Player1, Player2 = game(Player1, Player2)

lst = Player1 if winner == 1 else Player2
total = 0
for k, v in enumerate(lst):
  total += (len(lst) - k)*v

print(total)
