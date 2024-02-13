
def print_poly(fx):
    poly_str = "f(x) = "

    for i in range(len(fx)):
        term = fx[i][0]  # 항 차수
        coef = fx[i][1]  # 계수

        if (coef >= 0):
            poly_str += "+"
        poly_str += str(coef) + "x^" + str(term) + " "

    return poly_str


def calc_poly(x_value, fx):
    value = 0
    for i in range(len(fx_list)):
        term = fx[i][0]
        coef = fx[i][1]
        value += coef * x_value ** term
    return value


fx_list = [[300,7],[20,-4],[0,5]]

if __name__ == "__main__":
    pstr = print_poly(fx_list)
    print(pstr)
    x_value = int(input("X 값-->"))
    result = calc_poly(x_value, fx_list)
    print(result)
