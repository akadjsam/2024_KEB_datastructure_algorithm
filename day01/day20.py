def print_poly(t_x, f_x) -> str:
    """
    다항식 출력
    :param f_x:
    :return tpye -> str:
    """
    term = len(f_x) - 1
    poly_expression = "f(x) = "

    for i in range(len(fx)):
        term = t_x[i]
        coefficient = f_x[i]
        if coefficient > 0 and i!=0:
            poly_expression += "+"
        if coefficient != 0:
            poly_expression += f'{coefficient}x^{term} '
    return poly_expression


def calculation_poly(x_val, f_x) -> int:
    ret_value = 0
    #term = len(f_x) - 1

    for i in range(len(fx)):
        coefficient = f_x[i]  # 계수
        ret_value += coefficient * x_val ** tx[i]
        #term -= 1

    return ret_value
tx = [300, 20, 0]
fx = [7, -4, 5]

if __name__ == "__main__":
    print(print_poly(tx,fx))
    print(calculation_poly(int(input("X 값 : ")), fx))


