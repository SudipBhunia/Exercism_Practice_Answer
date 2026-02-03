def spiral_matrix(size):
    if size == 0:
        return []
    result = [[0] * size for _ in range(size)]
    row_begin = col_begin = 0
    row_end = col_end = size-1
    num = 1
    while(row_begin <= row_end and col_begin <= col_end):
        for col in range(col_begin, col_end+1):
            result[row_begin][col] = num
            num += 1
        row_begin += 1
        for row in range(row_begin, row_end+1):
            result[row][col_end] = num
            num += 1
        col_end -= 1
        if(row_begin <= row_end):
            for col in range(col_end, col_begin - 1,-1):
                result[row_end][col] = num
                num += 1
        row_end -= 1
        if(col_begin <= col_end):
            for row in range(row_end, row_begin - 1,-1):
                result[row][col_begin] = num
                num += 1
        col_begin+=1
    return result