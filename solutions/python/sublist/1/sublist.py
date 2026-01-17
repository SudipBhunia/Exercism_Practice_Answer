# Module-level constants (exported)
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    """
    Determine the relationship between two lists.
    
    Returns:
        SUBLIST: if list_one is a sublist of list_two
        SUPERLIST: if list_one is a superlist of list_two
        EQUAL: if both lists are equal
        UNEQUAL: if none of the above
    """
    # Check if lists are equal
    if list_one == list_two:
        return EQUAL
    
    # Check if list_one is a sublist of list_two
    if is_sublist(list_one, list_two):
        return SUBLIST
    
    # Check if list_one is a superlist of list_two
    if is_sublist(list_two, list_one):
        return SUPERLIST
    
    # Otherwise, they are unequal
    return UNEQUAL


def is_sublist(smaller, larger):
    """
    Check if 'smaller' is a contiguous subsequence of 'larger'.
    
    Returns True if smaller is found within larger, False otherwise.
    """
    # Empty list is a sublist of any list
    if not smaller:
        return True
    
    # If smaller is longer than larger, it can't be a sublist
    if len(smaller) > len(larger):
        return False
    
    # Check all possible positions in larger
    for i in range(len(larger) - len(smaller) + 1):
        # Check if smaller matches at position i
        if larger[i:i + len(smaller)] == smaller:
            return True
    
    return False