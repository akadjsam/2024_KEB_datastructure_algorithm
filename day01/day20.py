import tkinter as tk


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

# n = int(input("input : ")) #input box로 대체
# print(f'f({n}) = {fibo_memoization(n)}') #Label로 대체

if __name__ == '__main__':
    w = tk.Tk() #create window object
    w.title("Fibonacci")
    w.geometry("300x150")

    #create widget
    ldl_dissplay_fibo_result = tk.Label(w, text='Fibonacci by memoization')
    en_input_number = tk.Entry(w,)
    btn_click = tk.Button(w, text="Click")

    #
    ldl_dissplay_fibo_result.pack()
    en_input_number.pack(fill='x')
    btn_click.pack(fill='x')


    w.mainloop()