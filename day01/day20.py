# def factorial(n):
#     if n <= 0:
#         return 1
#     elif n == 1:
#         return n
#     else:
#         return n * factorial(n-1)
#
# def nCr(n,r) -> int:
#     return factorial(n) / (factorial(n-r) * factorial(r))
#
# print(nCr(7,0))

def factorial(n):
    pass
def nCr(n,r) -> int:
    """
    조합 함수
    :param n:
    :param r:
    :return : int:
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator / denominator

if __name__ == "__main__":
    n = int(input("Input n: "))
    r = int(input("Input r: "))

    print(f'{n}C{r} = {nCr(n,r)}')