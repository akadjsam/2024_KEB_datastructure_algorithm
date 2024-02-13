## 함수 선언 부분 ##
def is_queue_full() :
    global size, queue, front, rear
    if (rear != size-1) :
        return False
    elif (rear == size - 1) and (front == -1) :
        return True
    else:
        for i in range(front+1, size) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def is_queue_empty() :
    global size, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def en_queue(data) :
    global size, queue, front, rear
    if (is_queue_full()) :
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def de_queue() :
    global size, queue, front, rear
    if (is_queue_empty()) :
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    for i in range(size - 1):
        queue[i] = queue[i+1]
    queue[rear] = None
    return data

def peek() :
    global size, queue, front, rear
    if (is_queue_empty()) :
        print("큐가 비었습니다.")
        return None
    return queue[front+1]

size = 5
queue = ['정국','뷔','지민','진','슈가']
front = -1
rear = 4

if __name__ == "__main__" :
    for i in range(size + 1):
        print(f'대기줄 상태 : {queue}')
        de_queue()
    print("프로그램 종료!")