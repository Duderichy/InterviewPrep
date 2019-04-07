# this might be backwards in some regards

def mat_zero(matrix):
    # matrix[column][row]
    columns = set()
    rows = set()
    row_num = len(matrix)
    col_num = len(matrix[0])

    for i in range(row_num):
        for j in range(col_num):
            if matrix[i][j] == 0:
                columns.add(i)
                rows.add(j)
                break_now = True
                break
    
    test = False
    if test:
        return (columns, rows)

    for i in range(row_num):
        for j in range(col_num):
            if i in rows or j in columns:
                matrix[i][j] = 0

    return (columns, rows)


if __name__=="__main__":
    test_mat = [[1 for x in range(20)] for y in range(30)]
    print(test_mat)
    print(mat_zero(test_mat))
    test_mat[5][6] = 0
    print(mat_zero(test_mat))
    print(test_mat)
    test_mat[8][9] = 0
    print(mat_zero(test_mat))
    print(test_mat)
