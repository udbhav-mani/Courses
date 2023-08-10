class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items = [item] + self.items

    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head


st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)

print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
