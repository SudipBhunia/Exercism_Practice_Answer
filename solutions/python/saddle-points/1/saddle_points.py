def saddle_points(matrix):
    if not matrix:
        return []

    # Validate matrix
    first_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_length:
            raise ValueError("irregular matrix")

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Pre-compute max in each row and min in each column
    max_in_rows = [max(row) for row in matrix]
    min_in_cols = [min(matrix[r][c] for r in range(rows)) for c in range(cols)]

    saddle_points_list = []
    for row_idx in range(rows):
        for col_idx in range(cols):
            value = matrix[row_idx][col_idx]
            if value == max_in_rows[row_idx] and value == min_in_cols[col_idx]:
                saddle_points_list.append({"row": row_idx + 1, "column": col_idx + 1})

    return saddle_points_list