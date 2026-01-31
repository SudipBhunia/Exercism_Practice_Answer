"""Two-fer exercise: return a phrase sharing one item with someone else."""

def two_fer(name: str = "you") -> str:
    """Return the classic 'two-fer' phrase.

    Args:
        name: Person to share with. Defaults to "you".

    Returns:
        A string in the form: "One for <name>, one for me."
    """
    return f"One for {name}, one for me."