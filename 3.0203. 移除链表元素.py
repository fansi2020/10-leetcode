#AI的答案
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
       # 创建一个虚拟头节点，简化边界情况的处理
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                # 如果下一个节点的值等于 val，将下一个节点跳过
                current.next = current.next.next
            else:
                # 否则继续遍历
                current = current.next

        return dummy.next

        