def convert(input_grid):
    # Define the digit patterns (3 cols x 4 rows each)
    DIGITS = {
        (" _ "
         "| |"
         "|_|"
         "   "): "0",
        
        ("   "
         "  |"
         "  |"
         "   "): "1",
        
        (" _ "
         " _|"
         "|_ "
         "   "): "2",
        
        (" _ "
         " _|"
         " _|"
         "   "): "3",
        
        ("   "
         "|_|"
         "  |"
         "   "): "4",
        
        (" _ "
         "|_ "
         " _|"
         "   "): "5",
        
        (" _ "
         "|_ "
         "|_|"
         "   "): "6",
        
        (" _ "
         "  |"
         "  |"
         "   "): "7",
        
        (" _ "
         "|_|"
         "|_|"
         "   "): "8",
        
        (" _ "
         "|_|"
         " _|"
         "   "): "9",
    }
    
    # Validate input - check number of rows
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    # Validate input - check number of columns
    if input_grid:
        # Check if any row has length not divisible by 3
        for row in input_grid:
            if len(row) % 3 != 0:
                raise ValueError("Number of input columns is not a multiple of three")
    
    # Process the grid in chunks of 4 rows
    result = []
    
    for row_start in range(0, len(input_grid), 4):
        # Get 4 rows for this line of digits
        four_rows = input_grid[row_start:row_start + 4]
        
        # Number of digits in this line (each digit is 3 columns wide)
        num_digits = len(four_rows[0]) // 3
        
        line_result = ""
        
        # Process each digit (3 columns at a time)
        for col_start in range(0, len(four_rows[0]), 3):
            # Extract 3x4 cell for this digit
            cell = ""
            for row in four_rows:
                # Ensure we have exactly 3 characters (pad if necessary)
                segment = row[col_start:col_start + 3]
                # Pad to 3 characters if needed
                segment = segment.ljust(3)
                cell += segment
            
            # Look up the digit
            digit = DIGITS.get(cell, "?")
            line_result += digit
        
        result.append(line_result)
    
    return ",".join(result)


# Test examples
if __name__ == "__main__":
    # Test 1: Single line of digits "1234567890"
    test1 = [
        "    _  _     _  _  _  _  _  _ ",
        "  | _| _||_||_ |_   ||_||_|| |",
        "  ||_  _|  | _||_|  ||_| _||_|",
        "                              "
    ]
    print(convert(test1))  # Should print: 1234567890
    
    # Test 2: Multiple lines "123,456,789"
    test2 = [
        "    _  _ ",
        "  | _| _|",
        "  ||_  _|",
        "         ",
        "    _  _ ",
        "|_||_ |_ ",
        "  | _||_|",
        "         ",
        " _  _  _ ",
        "  ||_||_|",
        "  ||_| _|",
        "         "
    ]
    print(convert(test2))  # Should print: 123,456,789
    
    # Test 3: Invalid input (not multiple of 4 rows)
    try:
        convert(["   ", "  |", "  |"])
    except ValueError as e:
        print(f"Error: {e}")
    
    # Test 4: Unrecognizable character
    test4 = [
        "   ",
        "  |",
        "   ",
        "   "
    ]
    print(convert(test4))  # Should print: ?