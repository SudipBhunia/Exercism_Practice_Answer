def encode(numbers):
    result = []

    for number in numbers:
        if number < 0:
            raise ValueError("negative numbers not supported")

        groups = []

        # Split into 7-bit groups (LSB first)
        while True:
            groups.append(number & 0x7F)
            number >>= 7
            if number == 0:
                break

        # Reverse to MSB → LSB order
        groups.reverse()

        # Set continuation bit on all but last
        for i in range(len(groups) - 1):
            groups[i] |= 0x80

        result.extend(groups)

    return result


def decode(bytes_):
    numbers = []
    value = 0
    expecting_more = False

    for byte in bytes_:
        value = (value << 7) | (byte & 0x7F)

        if byte & 0x80:
            expecting_more = True
        else:
            numbers.append(value)
            value = 0
            expecting_more = False

    # If last value never terminated
    if expecting_more:
        raise ValueError("incomplete sequence")

    return numbers
