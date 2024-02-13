array_list = [('다현',200),('정연',150),('쯔위',90),
              ('사나',30),('지효',15)]

a = ('미나',40)

for i in range(len(array_list)):
    if array_list[i][1] <= a[1]:
        array_list.insert(i,a)
        break

print(array_list)