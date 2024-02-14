## 함수 선언 부분 ##
def is_queue_full() :
    global size, queue, front, rear
    if (rear + 1) % size == front:
        return True
    else :
        return False

def is_queue_empty() :
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def en_queue(data):
    global size, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear + 1) % size
    queue[rear] = data

def de_queue():
    global size, queue, front, rear
    if (is_queue_empty()) :
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global size, queue, front, rear
    if (is_queue_empty()) :
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % size]

def checking_wait_time():
    time = 0
    for i in range(1,len(queue)):
        if queue[i] != None:
            time += queue[i][1]
    print(f'대기시간이 {time}분 남았습니다.')

size = int(input("큐의 크기를 입력하세요 ==> "))
queue = [None for _ in range(size)]
front = rear = 0

if __name__ == "__main__" :
    en_queue(['사용', 9])
    en_queue(['고장', 3])
    print(queue)
    checking_wait_time()

    print("프로그램 종료!")
