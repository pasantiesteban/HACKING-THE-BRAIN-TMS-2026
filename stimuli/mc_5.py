def is_leap(year: int) -> bool:
    """
    Determines whether a given year is a leap year.
    
    Args:
        year: The year to check.
    
    Returns:
        True if it's a leap year, False otherwise.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

# Uncomment the minimal set of tests that achieve complete statement coverage:
# assert not is_leap(2021)
# assert is_leap(2016)
# assert is_leap(2020)
# assert is_leap(2000)
# assert not is_leap(1900)
