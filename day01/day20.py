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

def factorial(n) -> int: #
    # result = 1
    # for i in range(1,n+1):
    #     result *= i
    # return result
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1) #파이썬의 경우는 재귀함수를 많이 호출하게 되면 자동으로 에러를 발생시킨다.(1000번까지 발생)

def nCr(n,r) -> int:
    """
    조합 함수
    :param n:
    :param r:
    :return : int:
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)

if __name__ == "__main__":
    n = int(input("Input n: "))
    r = int(input("Input r: "))

    print(f'{n}C{r} = {nCr(n,r)}')