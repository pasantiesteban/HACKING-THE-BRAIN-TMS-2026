def abs_accel(start: float, end: float, time: float) -> float | None:
    """
    Computes the absolute acceleration between two speeds.
    
    Args:
        start: The initial speed.
        end: The final speed.
        time: The time interval.
    
    Returns:
        The absolute acceleration, or None if time is 0.
    """
    if time == 0:
        return None
    
    acceleration = 0
    if start != end:
        if start > end:
            acceleration = (start - end) / time
        else:
            acceleration = (end - start) / time
    return acceleration

# Uncomment the minimal set of tests that achieve complete statement coverage:
# assert abs_accel(10, 0, 10) == 1.0
# assert abs_accel(10, 0, 0) is None
# assert abs_accel(-1, -1, 2) == 0.0
# assert abs_accel(1, 1, 1) == 0.0
# assert abs_accel(0, 10, 10) == 1.0
