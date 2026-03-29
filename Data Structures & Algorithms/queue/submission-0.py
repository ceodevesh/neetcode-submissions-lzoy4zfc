class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.right
        new_node.prev = self.right.prev
        self.right.prev.next = new_node
        self.right.prev = new_node


        

        
        

    def appendleft(self, value: int) -> None:
        new_node =ListNode(value)
        new_node.next = self.left.next
        new_node.prev = self.left
        self.left.next.prev = new_node
        self.left.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        target = self.right.prev
        target_prev = target.prev
        target_prev.next = self.right
        self.right.prev = target_prev
        return target.val
        
        
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        target = self.left.next
        target_next = target.next
        self.left.next = target_next
        target_next.prev = self.left
        return target.val

        
