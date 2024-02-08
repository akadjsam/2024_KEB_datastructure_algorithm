def print_poly(p_x) -> str:
    """
    다항식 출력
    :param p_x:
    :return tpye -> str:
    """
    term = len(p_x) - 1
    poly_expression = "f(x) = "

    for i in range(len(fx)):
        coefficient = p_x[i]

        if coefficient >= 0:
            poly_expression += "+"
        poly_expression += f'{coefficient}x^{term} '
        term -= 1

    return poly_expression


def calculation_poly(x_val, f_x) -> int:
    ret_value = 0
    term = len(f_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(fx)):
        coefficient = f_x[i]  # 계수
        ret_value += coefficient * x_val ** term
        term -= 1

    return ret_value

fx = [2, 3, 5, 0, -9]

if __name__ == "__main__":
    print(print_poly(fx))
    print(calculation_poly(int(input("X 값 : ")), fx))


