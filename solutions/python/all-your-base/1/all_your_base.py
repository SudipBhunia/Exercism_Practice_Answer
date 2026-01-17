def rebase(input_base, digits, output_base):
    """
    Convert a number from one base to another.

    Args:
        input_base: The base of the input number (must be >= 2)
        digits: List of digits in the input base
        output_base: The base to convert to (must be >= 2)

    Returns:
        List of digits in the output base

    Raises:
        ValueError: If bases are invalid or digits are out of range
    """
    # Validate input base
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # Validate output base
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Validate digits
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # Handle empty input or all zeros
    if not digits or all(d == 0 for d in digits):
        return [0]

    # Step 1: Convert from input_base to base 10 (decimal)
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * input_base + digit

    # Step 2: Convert from base 10 to output_base
    if decimal_value == 0:
        return [0]

    result = []
    while decimal_value > 0:
        remainder = decimal_value % output_base
        result.append(remainder)
        decimal_value = decimal_value // output_base

    # Reverse because we built it backwards
    return result[::-1]

print(rebase(10, [5], 2))