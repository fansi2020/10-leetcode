#自己的答案
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        
        while cur:
            new = Node(cur.val,None)
            rcur = cur.random
            new.random = Node(rcur.val) #仅仅赋值了，没有建立指针
            new = new.next
            cur =cur.next
            
        return  new.next
#AI的答案
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 第一遍遍历：创建新节点并将其插入原链表的每个节点后面
        current = head
        while current:
            new_node = Node(current.val, None)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # 第二遍遍历：设置新节点的random指针
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # 第三遍遍历：恢复原链表，同时构建深拷贝链表
        current = head
        new_head = head.next
        new_current = new_head
        while current:
            current.next = new_current.next
            current = current.next
            if current:
                new_current.next = current.next
            new_current = new_current.next

        return new_head
