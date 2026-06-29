def first_even(nums: list[int]) -> int | None:
    """
    Finds the first even number in an array.
    
    Args:
        nums: A list of integers.
    
    Returns:
        The first even number, or None if none exist.
    """
    for num in nums:
        if num % 2 == 0:
            return num
    return None

# Uncomment the minimal set of tests that achieve complete statement coverage:
# assert first_even([1, 3, 5]) is None
# assert first_even([1, 2, 3]) == 2
# assert first_even([1]) is None
# assert first_even([4]) == 4
# assert first_even([]) is None
