import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper

def factorial(n) -> int:
    # result = 1
    # for i in range(1,n+1):
    #     result *= i
    # return result
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1) #파이썬의 경우는 재귀함수를 많이 호출하게 되면 자동으로 에러를 발생시킨다.(1000번까지 발생)
    # 재귀함수는 스택메모리 사용

@timer
def nCr(n,r) -> int: #SRP, OCP
    """
    조합 함수
    :param n:
    :param r:
    :return : int:
    """

    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)

    return int(numerator / denominator)