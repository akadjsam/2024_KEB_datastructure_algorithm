def fibo_recursion(n : int) -> int:
    """
    fibonacci function by recursion
    :param n: int
    :return: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)

def fibo_repetition(number : int) -> int:
    a = 0
    b = 1
    for _ in range(number):
        a,b = b, a+b
    return a

# memo = [None for _ in range(100)]
# memo[0] = 0
# memo[1] = 1
#memo = [0 if i==0 else 1 if i==1 else None for i in range(100)]
memo = [0,1] + [None] * (100-1)
def fibo_memoization(number : int, memo) -> int:
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
        result = fibo_memoization(number-1,memo) + fibo_memoization(number-2,memo)
    memo[number] = result
    return result

n = int(input("input : "))

for i in range(0, n):
    print(fibo_memoization(i,memo), end=' ')

# print()
# for i in range(0, 40):
#     print(fibo_recursion(i), end=' ')
# print()
# for i in range(0, 40):
#     print(fibo_repetition(i), end=' ')