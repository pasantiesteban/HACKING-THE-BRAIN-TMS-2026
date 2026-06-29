def shipping_fee(weight: float, distance: float) -> float | None:
    """
    Calculates a basic shipping fee based on package weight and distance.
    
    Args:
        weight: The package weight in kilograms.
        distance: The shipping distance in kilometers.
    
    Returns:
        The shipping fee, or None if invalid input.
    """
    if weight <= 0 or distance <= 0:
        return None
    fee = 5  # base fee
    if weight > 10:
        fee += 10
    if distance > 100:
        fee += 15
    return fee

# Uncomment the minimal set of tests that achieve complete statement coverage:
# assert shipping_fee(5, 50) == 5.0
# assert shipping_fee(0, 100) is None
# assert shipping_fee(15, 50) == 15.0
# assert shipping_fee(5, 150) == 20.0
# assert shipping_fee(15, 150) == 30.0
