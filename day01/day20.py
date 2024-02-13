def check_bracket(expr : str) -> bool:
    """
    :param expr: str
    :return: bool
    """
    stack = []
    table = {")": "(", "]": "[", "}": "{", ">": "<"}
    for char in expr:
        if char in table.values():
            stack.append(char)
        elif char in table.keys():
            if not stack or table[char] != stack.pop():
                print("!")
                return False
        else:
            pass
    return len(stack) == 0

## 전역 변수 선언 부분 ##
size = 20
stack = [None for _ in range(size)]
top = -1

## 메인 코드 부분 ##
if __name__ == "__main__":
    expression = input("Input expression : ")
    print(check_bracket(expression))