''' When importing objects from a module in Python, the syntax usually is as follows:

        from module_name import object

    Given  a string of an incorrect import statement, return the fixed string.
    All import statements will be the wrong way around. '''

def fix_import(s):
    new_lst = s.split(' ')
    return new_lst[2] + ' ' + new_lst[3] + ' ' + new_lst[0] + ' ' + new_lst[1]


print(fix_import("import object from module_name"))