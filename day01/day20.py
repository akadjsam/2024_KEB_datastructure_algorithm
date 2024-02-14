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
for i in range(0, 20):
    print(fibo_recursion(i), end=' ')
print()
for i in range(0, 20):
    print(fibo_repetition(i), end=' ')
