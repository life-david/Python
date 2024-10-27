#khoi tao ma tran ket qua
matrix1=[[1, 3, 4],
         [2, 8, 7]]
matrix2=[[2, 4, 6, 9],
         [1, 5, 8, 1],
         [2, 7, 7, 8]] 
         
#khoi tao tao ket qua
result=[[0, 0, 0, 0],
        [0, 0, 0, 0]]
#nhan hai ma tran
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for l in result:
    print(l)