import math
from math import log2

import mymath
import time
import random
if __name__ == "__main__":
    rangenumber = int(input("범위를 지정하세요 : "))
    answer = random.randrange(1, rangenumber+1)
    n = count = math.ceil(log2(rangenumber))
    print(count)
    while count != 0:
        count -= 1
        number = int(input("답을 유추하세요 : "))
        if number == answer:
            print("정답입니다.")
            break
        elif number < answer:
            print("up!")
        else:
            print("down!")
    else:
        print(f"정답을 맞추지 못했습니다. 정답은 {answer} 입니다.")
    print(f'시도횟수는 : {n-count} 입니다.')

