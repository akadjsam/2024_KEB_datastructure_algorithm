#memo = [0 if i==0 else 1 if i==1 else None for i in range(100)]
memo = [0,1] + [None] * (100-1)
def fibo_memoization(number : int) -> int:
    """
    fibonacci function by recursion with memoization
    :param n: int
    :return: int
    """
    if memo[number] is not None:
        return memo[number]
    if number < 2:
        result = number
    else:
        result = fibo_memoization(number-1) + fibo_memoization(number-2)
    memo[number] = result
    return result

n = int(input("input : "))

print(f'f({n}) = {fibo_memoization(n)}')
