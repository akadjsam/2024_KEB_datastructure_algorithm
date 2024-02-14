def decimal_to_octal(number:int) -> str:
    """
    decimal -> octal
    :param number: int
    :return: str
    """
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(number//8) + str(number%8)

print(decimal_to_octal(100))