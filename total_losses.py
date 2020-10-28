''' you just returned homet to find your mansion has been robbed! Given
    a dictionary of the stolen items, return the total amount of the burglary(number).
    If nothing was robbed, return the string "Lucky you!".'''


def calculate_losses(items):
    if bool(items) == False:
       return "Lucky you!"
    else:
        return sum(dict.values(items))

print(calculate_losses({
  "tv" : 30,
  "skate" : 20,
  "stereo" : 50,
}))

print(calculate_losses({
  "painting" : 20000,
}))

print(calculate_losses({}))