stone_list = []

print("과자집에 가는길 -> ",end='')
for i in range(6):
    stone = chr(ord('A')+i)
    stone_list.append(stone)
    print(stone, end=' ')
print("-> 과자집")

print("우리집에 오는길 -> ",end='')
for i in range(6):
    print(stone_list.pop(),end=' ')
print("-> 우리집")