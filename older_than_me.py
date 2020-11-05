''' Create a method in the Person class which returns how another person's age compares. Given
    the objects p1, p2 and p3, which will be initialised with the attributes name and age, return
    a sentence in the follwing format:

    {other_person} is {older than/ younger than / the same age as} me.
    '''

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def compare_age(self, other):
		if self.age > other.age:
			return other.name+ ' is older than me.'
		elif self.age < other.age:
			return other.name + ' is younger than me.'
		elif self.age == other.age:
			return other.name + ' is same age as mine.'

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

print(p1.compare_age(p2))
print(p1.compare_age(p3))
