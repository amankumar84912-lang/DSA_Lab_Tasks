class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

front = rear = None

def insert_front(x):
    global front, rear
    n = Node(x)

    if front is None:
        front = rear = n
    else:
        n.next = front
        front.prev = n
        front = n

def insert_rear(x):
    global front, rear
    n = Node(x)

    if rear is None:
        front = rear = n
    else:
        n.prev = rear
        rear.next = n
        rear = n

def delete_front():
    global front, rear

    if front is None:
        print("Deque is empty")
        return

    print("Deleted:", front.data)
    front = front.next

    if front:
        front.prev = None
    else:
        rear = None

def delete_rear():
    global front, rear

    if rear is None:
        print("Deque is empty")
        return

    print("Deleted:", rear.data)
    rear = rear.prev

    if rear:
        rear.next = None
    else:
        front = None

def display():
    temp = front
    print("Deque:", end=" ")

    while temp:
        print(temp.data, end=" ")
        temp = temp.next

    print()


insert_rear(10)
insert_rear(20)
insert_front(5)

display()

delete_front()
delete_rear()

display()