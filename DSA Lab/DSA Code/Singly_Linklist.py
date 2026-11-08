class Node:
    def __init__(self, data):
        self.data = data
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

def delete(value):
    global head
    temp = head
    prev = None

    while temp and temp.data != value:
        prev = temp
        temp = temp.next

    if temp is None:
        print("Element not found")
        return

    if prev is None:
        head = temp.next
    else:
        prev.next = temp.next

def display():
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

n = int(input("Enter number of nodes: "))
for i in range(n):
    insert(int(input()))

print("\nOriginal List:")
display()

x = int(input("Enter element to delete: "))
delete(x)

print("\nList after deletion:")
display()