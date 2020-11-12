# Write a function that maps files to their extension names.

def get_extension(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i.split('.')[1])
    return new_lst

print(get_extension(["code.html", "code.css"]))
print(get_extension(["project1.jpg", "project1.pdf", "project1.mp3"]))
print(get_extension(["ruby.rb", "cplusplus.cpp", "python.py", "javascript.js"]))