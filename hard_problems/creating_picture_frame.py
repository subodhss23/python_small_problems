''' Create a function that takes a width, height and character and returns a picture frame as a 2d list.'''

def get_frame(w, h, ch):
    new_lst = []
    if w < 3 or h < 3:
        return 'invalid'
    else:
        for i in range(h):
            if i == 0 or i == h-1:
                new_lst.append([w*ch])
            else:
                new_lst.append([ch + ' '*(w-2) + ch])
    return new_lst

print(get_frame(4, 5, "#"))
print(get_frame(10, 3, "*"))
print(get_frame(1, 5, "0"))