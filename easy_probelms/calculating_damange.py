''' Create a function that takes damange and speed(attacks per second) and returns the amount of
    damange after a given time. '''

def damage(damage, speed, time):
    if damage < 0 or speed < 0:
        return 'invalid'
    else:
        if time == 'second':
            return damage * speed 
        elif time == 'minute':
            return damage * speed * 60
        elif time == 'hour':
            return damage * speed *  60 * 60

print(damage(40, 5, "second"))
print(damage(100, 1, "minute"))
print(damage(2, 100, "hour") )