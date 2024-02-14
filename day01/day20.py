def decimal_to_octal(number:int) -> str:
    """
    decimal -> octal
    :param number: int
    :return: str
    """
    octal = ""
    while number > 0:
        octal = str(number % 8) + octal
        number = number // 8
    return octal

print(decimal_to_octal(10))