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

def decimal_to_binary(number:int) -> str:
    """
    decimal -> octal
    :param number: int
    :return: str
    """
    if number < 2:
        return str(number)
    else:
        return decimal_to_binary(number//2) + str(number%2)

def decimal_to_hex(number:int) -> str:
    """
    decimal -> hex
    :param number: int
    :return: str
    """
    if number < 16:
        if number >= 10:
            return chr(ord('A')+(number-10))
        else:
            return str(number)
    else:
        if number%16 >= 10 and number%16 < 16:
            return decimal_to_hex(number // 16) + chr(ord('A')+(number%16 - 10))
        else:
            return decimal_to_hex(number//16) + str(number%16)

print(decimal_to_binary(100))
