def get_matrix(n,m,value):
    print(n,m,value)
    matrix = []
    for i in range(n):
       row = []
       for _ in range(m):
           row.append(value)
           matrix.append(row)
           return matrix
result = get_matrix(3, 4, 7)