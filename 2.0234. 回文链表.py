#自己的答案
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new_list = ListNode(0) #它的值始终为0，而且没有为其创建节点
        new = new_list
        head2 = head
        new2 = new_list
        while new_list: #循环条件 while new_list 是不正确的，应该使用 while head 来遍历原始链表。
            new.val = head.val #语法，无法赋值
            new = new.next
            head = head.next
        
        pre = None
        cur = new #不能写成cur = new.next  一定要写成cur = new_list.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        while head: #没有定义new2和head2，无法使用val
            if new2.val != head2.val:
                return False
            new2 = new2.next
            head2 = head2.next
        return True
#第一次修改
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new_list = ListNode(0)
        new = new_list

        cur = head
        while cur:
            new.next = ListNode(cur.val)
            new = new.next
            cur = cur.next
        
        pre = None
        cur = new_list.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        while head and pre:
            if head.val != pre.val:
                return False
            
            head = head.next
            pre = pre.next
        return not head and not pre
    
#AI的答案
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 创建一个空链表用于存储反转后的链表
        new_list = ListNode(0)
        new = new_list
        
        # 复制原链表到新链表
        current = head
        while current:
            new.next = ListNode(current.val)
            new = new.next
            current = current.next
        
        # 反转新链表
        reversed_head = None
        current = new_list.next
        while current:
            temp = current.next
            current.next = reversed_head
            reversed_head = current
            current = temp
        
        # 比较原链表和反转后的链表
        while head and reversed_head:
            if head.val != reversed_head.val:
                return False
            head = head.next
            reversed_head = reversed_head.next
        
        # 如果链表长度不同，说明不是回文链表
        return not head and not reversed_head
    
#更优解
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 使用快慢指针的方法移动到链表中点
        cur = slow = fast = head
        prev = None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # 反转前半部分链表
            head = cur
            cur = head.next
            head.next = prev
            prev = head.

        if fast is not None:
            slow = slow.next

        # 比较前半部分链表（已反转）和后半部分链表
        while slow is not None:
            if slow.val == head.val:
                slow = slow.next
                head = head.next
            else:
                return False

        return True
