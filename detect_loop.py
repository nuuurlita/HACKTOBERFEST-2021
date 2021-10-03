class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def detectLoopFunction(self):
        slow_p = fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                self.removeLoopfunction(slow_p)
                return 1
        return 0
    def removeLoopfunction(self, loop_node):
        ptr1 = self.head
        while(1):
            ptr2 = loop_node
            while(ptr2.next != loop_node and ptr2.next != ptr1):
                ptr2 = ptr2.next
                       
            if ptr2.next == ptr1 :  
                break
             
            ptr1 = ptr1.next
        ptr2.next = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
ll = LinkedList()
n=int(input("Enter the number of nodes: "))
for k in range(0,n):
   ele=int(input("Enter element "))
   ll.push(ele)

ll.head.next.next.next.next.next = ll.head.next.next
 
ll.detectLoopFunction()
 
print("Linked List after removing loop: ")
ll.printList()
