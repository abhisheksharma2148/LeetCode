class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        class Node:
            def __init__(self,val= [1], next =None):
                self.val=val
                self.next = next

        def pascal_list(list3: list)-> list:
            list2 = [a+b for a,b in zip([0]+list3,list3+[0])]
            return list2

        def display(head):
            curr = head
            elements = []
            while curr:
                elements.append(curr.val)
                curr = curr.next
            return elements

        head = Node([1])
        dummy = head

        for i in range(rowIndex):
            dummy.next = Node(pascal_list(dummy.val))
            dummy= dummy.next

        return(display(head)[rowIndex])
        
