''' Suppose you have a guest list of  students and the country they are from, stored as
    key-value pairs in a dictionary. 
    
    Write a function that takes in a name and returns a name tag, that should read:
    '''

GUEST_LIST = {
	"Randy": "Germany", 
	"Karla": "France", 
	"Wendy": "Japan", 
	"Norman": "England", 
	"Sam": "Argentina"
}

def greeting(name):
    if name not in GUEST_LIST:
        return "Hi! I'm a guest."
    return "Hi! I'm "+ name + ", and I'm from " + str(GUEST_LIST.get(name))+ '.'


print(greeting("Randy"))
print(greeting("Sam"))
print(greeting("Monti"))