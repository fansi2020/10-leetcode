class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 计算链表的长度
        size = 1
        cur = head
        while cur.next: #注意这里终止的条件是是cur.next 而非cur，即到最后一个停止，否则下面的cur.next将无法执行
            cur = cur.next
            size += 1
        
        # 将链表的尾部与头部相连，形成环状链表
        cur.next = head

        # 找到新的头节点位置
        new_head = head
        for _ in range(size - k % size - 1):
            new_head = new_head.next

        # 新的尾节点
        new_tail = new_head

        # 断开环状链表
        new_head = new_head.next
        new_tail.next = None

        return new_head
