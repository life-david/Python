def multiply_matrix(matrix1, matrix2):
    # kiểm tra kích thước ma trận có thể nhân được hay không
    if len(matrix1[0]) != len(matrix2):
        return "Không thể nhân hai ma trận này"

    # khởi tạo ma trận kết quả
    result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

    # nhân hai ma trận
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
matrix1 = [[6, 2, 9],
           [8, 4, 1],
           [5, 6, 6]]
matrix2 = [[3, 2],
           [4, 5],
           [2, 6]]

result = multiply_matrix(matrix1, matrix2)
print(result)