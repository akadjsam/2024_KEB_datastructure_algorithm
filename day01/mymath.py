import time

def factorial(n) -> int:
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
    # if n <= 1:
    #     return 1
    # else:
    #     return n * factorial(n-1) #파이썬의 경우는 재귀함수를 많이 호출하게 되면 자동으로 에러를 발생시킨다.(1000번까지 발생)
    # # 재귀함수는 스택메모리 사용

def nCr(n,r) -> int:
    """
    조합 함수
    :param n:
    :param r:
    :return : int:
    """
    start = time.time()
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    end = time.time()
    print(end - start) #단일책임의 원칙에 벗어남. 한 함수에 2가지의 역할을 하고 있음.
    return int(numerator / denominator)