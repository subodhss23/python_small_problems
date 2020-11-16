''' Create a function that counts the number of towers. '''

def count_towers(towers):
    count_t = []
    temp_lst = []
    for i in towers:
        temp_lst = i[0].split(' ')
        count_t.append(temp_lst.count('##'))
    return max(count_t)


print(count_towers([
  ["     ##         "],
  ["##   ##        ##"],
  ["##   ##   ##   ##"],
  ["##   ##   ##   ##"]
]))

print(count_towers([
  ["                         ##"],
  ["##             ##   ##   ##"],
  ["##        ##   ##   ##   ##"],
  ["##   ##   ##   ##   ##   ##"]
]))

print(count_towers([
  ["##"],
  ["##"]
]))