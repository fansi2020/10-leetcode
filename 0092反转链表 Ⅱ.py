#反转链表 II
#我的答案
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head#错误，没有初始化pre
        for _ in range (left):#错误，没有让pre移动到需要反转的节点之前
            cur = cur.next
        for left in range(right - left +1):#范围错误，应为(right - left)
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
            return head #错误，参见下面的回答
#AI 答案
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            nextnode = cur.next
            cur.next = nextnode.next
            nextnode.next = pre.next
            pre.next = nextnode
        return dummy.next 
