# the Luhn algorithm validates IDs, such as credit card numbers,
# SIM card numbers, even survey codes found on fast food company
# receipts.

def luhn(ID: int) -> int:
    """
    returns the checksum of ID, computed using the Luhn algorithm.
    """
    checksum = 0
    double = True
    while ID > 0:
        digit = ID % 10
        if double:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit

        ID //= 10
        double = not double
    return checksum % 10

print(luhn(int(input())))
