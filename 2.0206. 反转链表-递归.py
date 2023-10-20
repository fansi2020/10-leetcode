class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseLinkedList(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.reverseLinkedList(head.next)
        head.next.next = head
        head.next = None

        return new_head


#leetcode
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head