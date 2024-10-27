import numpy as np

def multiply_matrices(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# Example usage
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = multiply_matrices(a, b)
print(result)