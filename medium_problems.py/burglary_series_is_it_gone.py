''' Your spouse is not concerned with the loss of material possessions but rahter with 
    his/her favorite pet. Is it gone?!

    Given a dictionary of the stolen items and a string in lower cases respresenting the
    name of the pet(e.g. "rambo"), return:
    - "Rambo is gone..." if the name is on the list.
    - "Rambo is here!" if the anems is not on the list.

    Note that the first letter of the name in the return statement is capitalized.'''

def find_it(items, name):
    if name in items:
        return name.capitalize() + ' is gone...'
    else:
        return name.capitalize() + ' is here!'
        
print(find_it({
  "tv": 30,
  "stereo": 50,
	"julius": 100,											 
}, "julius"))

