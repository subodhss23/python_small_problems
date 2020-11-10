''' create a function to calculate the determinant of a 2 * 2
    matrix. The determinant of the following matrix is ad - bc: '''


def calc_determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]

print(calc_determinant([
  [5, 3],
  [3, 1]
])) 