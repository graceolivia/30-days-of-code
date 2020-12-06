class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
    # Complete this method
    # check along linked list until node.next == None
    # then insert the data node
    # return head
        if head is None:
            head = Node(data)
        else:
            node = head
            while(node.next !=None):
                node = node.next
            node.next = Node(data)
        return head

mylist= Solution()
