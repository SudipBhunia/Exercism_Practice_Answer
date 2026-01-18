def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('irregular matrix')

    row_max_li = list(map(max, matrix))
    col_min_li = list(map(min, list(zip(*matrix))))

    return [
        {'row': r+1, 'column': c+1}
        for r, row_max in enumerate(row_max_li)
        for c, col_min in enumerate(col_min_li)
        if row_max == col_min
    ]