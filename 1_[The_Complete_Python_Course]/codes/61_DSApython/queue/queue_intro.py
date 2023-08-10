class Queue:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head
    

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print(q.pop())
print(q.pop())