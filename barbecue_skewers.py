''' You are in charge of the barbecue grill. A vegeterian kewer is a kewer that has only vegetables(-o).
    A non-vegeterian skewer is a skewer with at least one piece of meat (-x).
    
    For example, the grill below has 4 non-vegetarian skewers and 1 vegeterian skewer(the one in the table).

    ["--xo--x--ox--",
    "--xx--x--xx--",
    "--oo--o--oo--",      <<< vegetarian skewer
    "--xx--x--ox--",
    "--xx--x--ox--"]

    Given a BBQ grill, write a function that returns [# vegeterian skewers, # non-vegetarian skewers].
    For example above, the funciton should return [1, 4].
    '''


def bbq_skewers(grill):
    veg = 0
    non = 0
    store = {}
    for i in grill:
        store = (set(i))
        if 'x' in store:
            non+=1
        else:
            veg+=1
    return [veg, non]

print(bbq_skewers([
  "--oooo-ooo--",
  "--xx--x--xx--",
  "--o---o--oo--",
  "--xx--x--ox--",
  "--xx--x--ox--"
]))

print(bbq_skewers([
  "--oooo-ooo--",
  "--xxxxxxxx--",
  "--o---",
  "-o-----o---x--",
  "--o---o-----"
]))