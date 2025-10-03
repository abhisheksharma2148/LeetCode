# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slowPointer, fastPointer = dummy, dummy
        while slowPointer and fastPointer:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next if fastPointer.next else None
        return slowPointer
