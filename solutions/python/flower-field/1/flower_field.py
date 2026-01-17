#%%
def annotate(minefield):
    # Validate input
    if not isinstance(minefield, list):
        raise ValueError("The board is invalid with current input.")

    # Empty board is valid
    if len(minefield) == 0:
        return []

    # Check all rows have the same length
    if len(minefield) > 0:
        row_length = len(minefield[0])
        for row in minefield:
            if len(row) != row_length:
                raise ValueError("The board is invalid with current input.")

    # Validate characters (only ' ' and '*' allowed)
    for row in minefield:
        for char in row:
            if char not in (' ', '*'):
                raise ValueError("The board is invalid with current input.")

    # If all rows are empty strings, return as is
    if all(row == '' for row in minefield):
        return minefield

    rows = len(minefield)
    cols = len(minefield[0]) if rows > 0 else 0

    # Create result board
    result = []

    # Direction offsets for 8 adjacent cells (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),           (0, 1),    # left, right
        (1, -1),  (1, 0),  (1, 1)     # bottom-left, bottom, bottom-right
    ]

    # Process each cell
    for r in range(rows):
        row_result = ""
        for c in range(cols):
            # If it's a flower, keep it
            if minefield[r][c] == '*':
                row_result += '*'
            else:
                # Count adjacent flowers
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check if neighbor is within bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if minefield[nr][nc] == '*':
                            count += 1

                # Add count or space
                if count > 0:
                    row_result += str(count)
                else:
                    row_result += ' '

        result.append(row_result)

    return result