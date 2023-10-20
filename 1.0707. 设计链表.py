

class MyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    class MyListNode:
        def __init__(self, val = 0, next = None):
            self.val = val
            self.next = next
    # 获取链表长度
    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next 
        return count
    # size = length(self) 链表长度的定义看self.size = 0
              
    def get(self,index: int) -> None: #这里加self的作用？让链表本身有定义  -> None的作用？
        count = 0
        cur = self.head
        while cur and count < index - 1:
            count += 1
            cur = cur.next
        if not cur:
            return '-1'
        # return cur.next #错误应为：return cur.val
        return cur.val

    def addAtHead(self, val) -> None:
        node = self.MyListNode(val) #错误，应为：node = self.MyListNode(val)，少了MyListNode
        node.next = self.head # 错误答案 MyLinkedList.Head = node.next
        self.head = node #这行的作用是声明node所在的指针为头元素，若无这行，无法在链表中显示出val
        self.size += 1

    def addAtTail(self, val) -> None:
        node = self.MyListNode(val) #缺失判断：如果链表里没有元素，if not self.head: （下一行）self.head = new_node
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.size += 1

    def addAtIndex(self, index: int, val):
        count = 0 #缺失判断：如果index不在链表里，小于零则排在表头，大于等于链表长度-1则排在表尾
        if index < 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index < self.size and index > 0:
            cur = self.head
            while cur and count < index - 1:
                count += 1
                self.cur = self.cur.next
            node = self.MyListNode(val) 
            # 错误答案MyLinkedList.cur = node
            # 错误答案node.next = MyLinkedList.cur.next
            node.next = cur.next
            cur.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:#不知道为什么这个函数只能删除头节点，其它节点都无法删除
        if index < 0 or index >= self.size:#没有考虑到头元素的特殊情况
            return
        if index == 0:
            self.head = self.head.next
        else:
            count = 0 
            cur = self.head
            #错误答案while MyLinkedList.cur and count < index - 2:
            while cur and count < index - 1:
                count += 1
                cur = cur.next
            if not cur: #缺失：如果索引index无效？例如index小于0 应改为 if index < 0: \\return \\elif index > self.length(self) return \\elif index == 0 self.head = self.head.next \\else \\while count < index - 1 cur = cur.next
                return 
            cur.next = cur.next.next #千万不能写成 cur = cur.next.next
        self.size -= 1



        
def printLinkedList(linkedList):
    cur = linkedList.head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
    

# 创建 MyLinkedList 的实例
linkedList = MyLinkedList()

# 执行一些操作来填充链表
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)
linkedList.deleteAtIndex(2)
#print(linkedList.get(0))
# 打印链表
printLinkedList(linkedList)

#AI答案
class MyLinkedList:

    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = self.ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = self.ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > 0 and index < self.size:
            new_node = self.ListNode(val)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
def printLinkedList(linkedList):
    current = linkedList.head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
    

# 创建 MyLinkedList 的实例
linkedList = MyLinkedList()

# 执行一些操作来填充链表
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)
linkedList.deleteAtIndex(2)
# 打印链表
printLinkedList(linkedList)