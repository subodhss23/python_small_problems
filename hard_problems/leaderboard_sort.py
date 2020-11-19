'''  Gvien an array of users, each defined by an object with the following properties: name, score, reputation
    create a function that sorts the array to form the correct leaderboard.

    The leaderboard takes into consideration the score of each user of course, but an emphasis is put on
    their reputation in the community, so to get the trueScore, you should add the reputation multiplied by 2
    to the score.

    Once you know the trueScore of each user, sort the array according to it in descending order.'''

def leaderboards(users):
    final_list = []
    new_obj = {}
    for i in users:
        trueScore = i['reputation'] * 2 + i['score']
        # new_list.append({trueScore: i})
        x = {trueScore : i}
        new_obj.update(x)
    temp_lst = []
    for i in new_obj.keys():
        temp_lst.append(i)
    x = sorted(temp_lst, reverse=True)
    for i in range(len(x)):
        final_list.append(new_obj[x[i]])
    return final_list
    



print(leaderboards([
  { "name": "a", "score": 100, "reputation": 20 },
  { "name": "b", "score": 90, "reputation": 40 },
  { "name": "c", "score": 115, "reputation": 30 },
]))