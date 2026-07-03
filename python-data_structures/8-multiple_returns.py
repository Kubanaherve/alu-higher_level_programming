#!/usr/bin/python3
def multiple_returns(sentence):
    """Return tuple of (length, first character) of a string."""
    if sentence:
        return (len(sentence), sentence[0])
    return (0, None)
