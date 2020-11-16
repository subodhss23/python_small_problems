''' In cricket, an over consists of six deliveries a boweler bowls from one end.
    Create a function that takes the number of balls balls bowled by a bowler and 
    calculates the number of overs  and balls bowled by him/her. Return the value
    as a float, in the format overs.balls.'''

def total_overs(balls):
    return balls // 6 + (balls % 6) / 10

print(total_overs(2400))
print(total_overs(164))
print(total_overs(945))
print(total_overs(5))