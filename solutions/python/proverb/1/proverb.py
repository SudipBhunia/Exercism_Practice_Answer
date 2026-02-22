def proverb(*items, qualifier=None):
    if not items:
        return []

    result = []

    # Generate middle lines
    for first, second in zip(items, items[1:]):
        result.append(f"For want of a {first} the {second} was lost.")

    # Generate final line
    first_item = items[0]

    if qualifier:
        result.append(f"And all for the want of a {qualifier} {first_item}.")
    else:
        result.append(f"And all for the want of a {first_item}.")

    return result