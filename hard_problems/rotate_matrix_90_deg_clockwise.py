'''Create a function that receives a square n*n matrix and return the matrix after it has been
    rotated 90 degrees in the clockwise direction.'''

def rotate(mat):
    new_lst = []
    N = len(mat[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = mat[i][j]
            mat[i][j] = mat[N - 1 - j][i]
            mat[N - 1 - j ][i] = mat[N - 1- j][N - 1 - j]
            mat[N - 1 - i ][N - 1 - j] = mat[j][N - 1 - i]
            mat[j][N - 1 - i ] = temp
    return mat


print(rotate([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))

print(rotate([
	["a", "b", "c"],
	["d", "e", "f"], 
	["g", "h", "i"]
]))