def factorial(n) -> int: #
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1) #파이썬의 경우는 재귀함수를 많이 호출하게 되면 자동으로 에러를 발생시킨다.(1000번까지 발생)
    #재귀함수는 스택메모리 사용
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