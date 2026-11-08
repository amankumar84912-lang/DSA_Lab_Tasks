class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = None

def insert(data):
    global head
    new = Node(data)

    if head is None:
        head = new
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

def delete(value):
    global head
    temp = head

    while temp and temp.data != value:
        temp = temp.next

    if temp is None:
        print("Element not found")
        return

    if temp.prev:
        temp.prev.next = temp.next
    else:
        head = temp.next

    if temp.next:
        temp.next.prev = temp.prev

def display():
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

n = int(input("Enter number of nodes: "))

print("Enter elements:")
for i in range(n):
    insert(int(input()))

print("\nOriginal List:")
display()

x = int(input("Enter element to delete: "))
delete(x)

print("\nList after deletion:")
display()