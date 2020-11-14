''' Given a square matrix(i.e. same number of rows as columns), its trace is the
    sum of the entries in the main diagonal(i.e. the diagonal line from the 
    top left to the bottom right). 
    
    write a function that takes a square matrix and computes its trace.
    '''

def trace(lst):
    counter = 0
    sum = 0
    for i in lst:
        sum += i[counter]
        counter+=1
    return sum



print(trace([
  [1, 4],
  [4, 1]
]))


print(trace([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))

print(trace([
  [1, 0, 1, 0],
  [0, 2, 0, 2],
  [3, 0, 3, 0],
  [0, 4, 0, 4]
]))