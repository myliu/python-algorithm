# http://www.futoshiki.org

m = [[1, 2, 2], [2, 3, 1], [3, 1, 2]]

# key is smaller than the value
order = {
    (0, 0) : (0, 1),
    (0, 1) : (0, 2),
    (1, 2) : (1, 1),
    #(0, 2) : (0, 1),
}

def futoshiki(matrix, order):
    # n is the number of rows
    n = len(matrix)
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] in rows[i] or matrix[i][j] in cols[j]:
                return False
                
            # (i, j) = (0, 2)
            if (i, j) in order:
                # (0, 1)
                # matrix[0][1] > matrix[0][2]
                target = order[(i, j)]
                if matrix[target[0]][target[1]] < matrix[i][j]:
                    return False
            
            rows[i].add(matrix[i][j])
            cols[j].add(matrix[i][j])
    return True

print futoshiki(m, order)