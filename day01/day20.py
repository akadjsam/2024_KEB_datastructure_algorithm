def bianry_search(arr, data):
    start = 0
    end = len(arr)-1
    while(start<=end):
        n = (start+end)//2
        if data == arr[n]:
            return n
        elif data > arr[n]:
            start = n+1
        else:
            end = n-1
    return -1
def search(arr, data):
    for i in range(len(arr)):
        print(arr[i], end=' ')
        if data == arr[i]:
            print()
            return i
    return -1

a = [1,2,3,4,5,6]
find_data = 4
print(search(a,find_data))
print(bianry_search(a,find_data))