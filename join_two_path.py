''' Write a function taht receives tow portions of a path and joins them. The portions
    will be joined with the "/" seperator. There could be only one separator and 
    if it is not present it should be added.'''

def join_path(portion1, portion2):
    return portion1.strip('/') + '/' + portion2.strip('/')

print(join_path("portion1", "portion2"))
print(join_path("portion1/", "portion2") )
print(join_path("portion1", "/portion2"))
print(join_path("portion1/", "/portion2"))