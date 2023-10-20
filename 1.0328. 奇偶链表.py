#自己的答案

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        odd_list = ListNode(0)
        even_list = ListNode(0)
        odd = odd_list
        even = even_list
        
        count = true #语法错误
        while head:
            if count
             odd.next = head
             head = head.next #思路错误，没让odd指针移动
            else:
                even.next = head
                head = head.next #思路错误，没让odd指针移动
            count = not cocunt
        even.next = None
        odd.next = even_list.next
        return odd_list #如果没有next，则会多一个0
#修改后
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        odd_list = ListNode(0)
        even_list = ListNode(0)
        odd = odd_list
        even = even_list
        
        count = True
        while head:
            if count:
             odd.next = head
             odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            count = not count
        even.next = None
        odd.next = even_list.next
        return odd_list.next


#AI答案

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        # 初始化奇数链表和偶数链表的头节点
        odd_head = ListNode(0)
        even_head = ListNode(0)
        
        # 初始化奇数链表和偶数链表的指针
        odd = odd_head
        even = even_head
        
        # 遍历原始链表并按位置将节点添加到奇数链表或偶数链表
        is_odd = True
        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            is_odd = not is_odd
        
        # 将奇数链表的末尾连接到偶数链表的头部
        odd.next = even_head.next
        even.next = None
        
        return odd_head.next
