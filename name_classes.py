''' Write a class called Name and create the following attributes
    given a first name and last name(as fname and lname): '''


class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.fullname = fname.capitalize() + ' '  + lname.capitalize()
        self.initials = fname[0].upper() + '.' + lname[0].upper()


al = Name('john', "Smith")
print(al.fname)
print(al.lname)
print(al.fullname)
print(al.initials)
