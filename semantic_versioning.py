''' In semantic versioning a piece of software can be represented in a format like
    this example:
    6.1.9
    1. The first number is the major version.
    2. The second number is the minor version.
    3. The third number is the patch(bug fixes).

    Create three separate functions, one to retrieve each element in the 
    semantic versioning specification.'''

def retrieve_major(semver):
    new_lst = semver.split('.')
    return new_lst[0]

def retrieve_minor(semver):
    return semver.split('.')[1]

def retrieve_patch(semver):
    return semver.split('.')[2]

print(retrieve_major("6.1.9"))
print(retrieve_minor("6.1.9"))
print(retrieve_patch("6.1.9"))