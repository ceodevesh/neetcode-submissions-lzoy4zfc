class MinStack:

    def __init__(self):
        self.new = []
        self.new_min = []
        

    def push(self, val: int) -> None:
        if not self.new_min or  val<=self.new_min[-1] :
            self.new_min.append(val)
        self.new.append(val)
        

    def pop(self) -> None:
        if self.new[-1] == self.new_min[-1]:
            self.new_min.pop()
        self.new.pop()
        

    def top(self) -> int:
        return self.new[-1]
        

    def getMin(self) -> int:
        return self.new_min[-1]
        
