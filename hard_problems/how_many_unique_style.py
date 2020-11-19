''' There are many different styles of music and many albums exhibit multiple styles. Create
    a function that takes a list of musical styles from albums and returns how many
    style are unique. '''

def unique_styles(albums):
    sum_result = 0
    new_lst = []
    for i in albums:
        x = i.split(',')
        for j in x:
            new_lst.append(j)
    return len(set(new_lst))

print(unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]))

# print(unique_styles([
#   "Soul",
#   "House,Folk",
#   "Trance,Downtempo,Big Beat,House",
#   "Deep House",
#   "Soul"
# ]))