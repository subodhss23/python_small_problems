''' Create a function that takes an old price old, a new price new, and returns
    what percent the price decreased or increased. Round the percentage to the 
    nearest whole percent.'''

def percentage_changed(old, new):
    old_old = int(old.strip('$'))
    new_new = int(new.strip('$'))
    if old_old > new_new:
        return (old_old - new_new) * 1
    elif new_new > old_old:
        return (new_new - old_old) * 1

print(percentage_changed("$800", "$600"))
print(percentage_changed("$1000", "$840"))
print(percentage_changed("$100", "$950"))