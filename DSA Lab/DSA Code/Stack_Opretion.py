stack = []

def priority(x):
    if x == '^':
        return 3
    if x in '*/%':
        return 2
    if x in '+-':
        return 1
    return 0

infix = input("Enter infix expression: ")
postfix = ""

for x in infix:
    if x.isalnum():
        postfix += x

    elif x == '(':
        stack.append(x)

    elif x == ')':
        while stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()

    else:
        while stack and priority(stack[-1]) >= priority(x):
            postfix += stack.pop()
        stack.append(x)

while stack:
    postfix += stack.pop()

print("Postfix expression:", postfix)