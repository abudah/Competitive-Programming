class MyQueue:

    def __init__(self):
        self.Instack=[]
        self.Outstack=[]        

    def push(self, x: int) -> None:
        self.Instack.append(x)

    def pop(self) -> int:
        if len(self.Outstack)==0:
            if len(self.Instack)==0:
                return "Cannot Dequeue from empty"
            while len(self.Instack)>0:
                last_element=self.Instack.pop()
                self.Outstack.append(last_element)
        return self.Outstack.pop()

    def peek(self) -> int:
        peek=self.pop()
        self.Outstack.append(peek)
        return peek
    
    def empty(self) -> bool:
        if len(self.Outstack)==0 and len(self.Instack)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()