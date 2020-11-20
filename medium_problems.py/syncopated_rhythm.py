''' Syncopation means an emphasis on a weak beat of a bar in music; most commonly, beat 2 and y( and all
    other even-numbered beats if applicable).

    s is a line of music, represented as a string, where hashtags # represent emphasized beat. Create a 
    function that returns if the line of music contains any syncopation.'''

# def has_syncopation(s):
#     return '#' in s[1::2]
       
def has_syncopation(s):
    if len(s) < 2:
        return False
    for i in range(len(s)):
        if s[i+1] == '#' or s.count('#') >= 4:
            return True
        else:
            return False

        
print(has_syncopation(".#.#.#.#"))
print(has_syncopation("#.#...#."))
print(has_syncopation("#.#.###."))