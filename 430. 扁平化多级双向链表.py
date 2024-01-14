class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                # 保存下一个节点
                next_node = curr.next
                # 扁平化子链表
                flattened_child = self.flatten(curr.child)
                # 连接当前节点和子链表
                curr.next = flattened_child
                flattened_child.prev = curr
                curr.child = None
                # 找到子链表的最后一个节点
                while curr.next:
                    curr = curr.next
                # 连接子链表和下一个节点
                curr.next = next_node
                if next_node:
                    next_node.prev = curr
            curr = curr.next
        return head
