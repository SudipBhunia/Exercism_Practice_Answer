def transpose(text):
    if not text:
        return ""
    
    lines = text.split('\n')
    max_length = max(len(line) for line in lines) if lines else 0
    
    result = []
    
    for col_index in range(max_length):
        column_chars = []
        for line in lines:
            if col_index < len(line):
                column_chars.append(line[col_index])
            else:
                column_chars.append(' ')
        
        result.append(''.join(column_chars))
    
    # Find the actual length each row needs to be (based on content below)
    min_lengths = [0] * len(result)
    
    for i in range(len(result) - 1, -1, -1):
        stripped = result[i].rstrip()
        if i == len(result) - 1:
            # Last row: just use its stripped length
            min_lengths[i] = len(stripped)
        else:
            # Other rows: at least as long as the row below
            min_lengths[i] = max(len(stripped), min_lengths[i + 1])
    
    # Now apply the minimum lengths
    for i in range(len(result)):
        stripped = result[i].rstrip()
        result[i] = stripped.ljust(min_lengths[i])
    
    return '\n'.join(result)