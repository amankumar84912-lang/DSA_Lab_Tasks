dq = []

def insert_front(x):
    dq.insert(0, x)

def insert_rear(x):
    dq.append(x)

def delete_front():
    if dq:
        print("Deleted:", dq.pop(0))
    else:
        print("Deque is empty")

def delete_rear():
    if dq:
        print("Deleted:", dq.pop())
    else:
        print("Deque is empty")

def display():
    print("Deque:", dq)


insert_rear(10)
insert_rear(20)
insert_front(5)

display()

delete_front()
delete_rear()

display()