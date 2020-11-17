''' Stalactites hang from the ceiling of a cave while stalagmites grow from the floor.

    Create a function that determines whether the input represents "stalactites" or "stalagmites"
    If it represents both, return "both". Input will be a 2D list with 1 representing a piece of
    rock, and 0 representing air space.'''

def mineral_formation(cave):
    if 1 in cave[0] and 1 in cave[len(cave)-1]:
        return 'both'
    elif 1 in cave[0]:
        return 'stalactites'
    elif 1 in cave[len(cave)-1] :
        return 'stalagmites'

print(mineral_formation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]))

print(mineral_formation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]))

print(mineral_formation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]))