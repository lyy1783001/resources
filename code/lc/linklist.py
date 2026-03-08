from typing import List, Optional


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def createLinkedList(arr:'List[int]') -> 'ListNode':
    if arr is None or len(arr) == 0:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1,len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head
'''arr = [1, 2, 3, 4, 5]
head = createLinkedList(arr)
cur = head
while cur is not None:
    print(cur.val)
    cur = cur.next'''

'''# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 在单链表头部插入一个新节点 0
p = head
head = ListNode(0)
head.next = p
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5

# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])'''

'''# 在单链表尾部插入一个新节点 6
head = createLinkedList([1, 2, 3, 4, 5])
p = head
# 先走到链表的最后一个节点
while p.next is not None:
    p=p.next
# 现在 p 就是链表的最后一个节点
# 在 p 后面插入新节点
p.next = ListNode(6)
# 现在链表变成了 1 -> 2 -> 3 -> 4 -> 5 -> 6'''

'''# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 在第 3 个节点后面插入一个新节点 66
# 先要找到前驱节点，即第 3 个节点
p = head
for i in range(2):
    p = p.next
#print(p.val)
# 此时 p 指向第 3 个节点
# 组装新节点的后驱指针
q = ListNode(66)
q.next = p.next
p.next = q

# 插入新节点


# 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5'''

'''# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])
p = head
# 删除第 4 个节点，要操作前驱节点
for i in range(2):
    p = p.next
p.next = p.next.next

# 此时 p 指向第 3 个节点，即要删除节点的前驱节点
# 把第 4 个节点从链表中摘除

# 现在链表变成了 1 -> 2 -> 3 -> 5'''

'''
# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 删除尾节点
p = head
# 找到倒数第二个节点
while p.next.next is not None:
    p = p.next
##print(p.val)
p.next=None
# 此时 p 指向倒数第二个节点
# 把尾节点从链表中摘除


# 现在链表变成了 1 -> 2 -> 3 -> 4'''


class DoubleListNode():
    def __init__(self,x):
        self.val = x
        self.next = None
        self.prev = None

def createDoublyLinkedList(arr: List[int]) -> Optional[DoubleListNode]:
    if not arr:
        return None
    head = DoubleListNode(arr[0])
    p = head
    for i in range(1, len(arr)):
        q = p
        p = DoubleListNode(arr[i])
        q.next = p
        p.prev = q
    return head

'''# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])
tail = None

# 从头节点向后遍历双链表
p = head
while p is not None:
    if p.next is None:
        tail = p
    print(p.val)
    p = p.next
p = tail
# 从尾节点向前遍历双链表
while p is not None:
    print(p.val)
    p = p.prev'''

'''head = createDoublyLinkedList([1, 2, 3, 4, 5])
# 在双链表头部插入新节点 0
p = DoubleListNode(0)
p.next = head
head.prev = p
head = p 
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5

# 创建一条双链表'''
'''head = createDoublyLinkedList([1, 2, 3, 4, 5])

p = head
tail = None
# 先走到链表的最后一个节点
while p is not None:
    tail = p
    p = p.next
print(tail.val)
# 在双链表尾部插入新节点 6
new_node = DoubleListNode(6)
# 更新尾节点引用
tail.next = new_node
new_node.prev = tail
tail = new_node
# 现在链表变成了 1 -> 2 -> 3 -> 4 -> 5 -> 6'''


'''# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])
p = head
# 想要插入到索引 3（第 4 个节点）
# 需要操作索引 2（第 3 个节点）的指针
for i in range(2):
    p = p.next
#print(p.val)
# 组装新节点
new_node = DoubleListNode(66)
new_node.next = p.next
new_node.prev = p
p.next.pre = new_node
p.next = new_node
# 插入新节点
# 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5'''


# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])
p = head
# 删除第 4 个节点
# 先找到第 3 个节点
for i in range(2):
    p = p.next

# 现在 p 指向第 3 个节点，我们将它后面的那个节点摘除出去
print(p.next.next.prev.val)
p.next.next.prev = p
p.next = p.next.next
q = head
while q is not None:
    print(q.val)
    q = q.next
# 把 toDelete 从链表中摘除


# 把 toDelete 的前后指针都置为 null 是个好习惯（可选）


# 现在链表变成了 1 -> 2 -> 3 -> 5