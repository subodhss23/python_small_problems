''' Given a list of scrabble title(as dictinoaries), create 
    a function that outputs the maximum possible score a player 
    can achieve by summing up the total number of points for all the
    titles in their hand. Each hand contains 7 scrabble tiles.'''

def maximum_score(title_hand):
    sum = 0
    # for i in range(len(title_hand)):
    #     sum = sum + (title_hand[i].get("score"))
    # return sum
    for i in title_hand:
        sum +=i['score']
    return sum
     


print(maximum_score([
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]))

print(maximum_score([
  { "tile": "B", "score": 2 },
  { "tile": "V", "score": 4 },
  { "tile": "F", "score": 4 },
  { "tile": "U", "score": 1 },
  { "tile": "D", "score": 2 },
  { "tile": "O", "score": 1 },
  { "tile": "U", "score": 1 }
]))