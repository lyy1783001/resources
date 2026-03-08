from linklist import ListNode


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

'''class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:'''
#预处理
l1 = createLinkedList([9,9,9,9])
l2 = createLinkedList([9,9,9,9,9,9,9])

#正式逻辑
a = 0  # 进位符
p1 = l1
p2 = l2
dummy = ListNode(-1)
p = dummy
while p1 and p2:
    sum = p1.val + p2.val + a
    p.next = ListNode(sum % 10)
    a = sum // 10
    p1 = p1.next
    p2 = p2.next
    p = p.next
while p1:
    sum = p1.val + a
    p.next = ListNode(sum % 10)
    a = sum // 10
    p1 = p1.next
    p = p.next
while p2:
    sum = p2.val + a
    p.next = ListNode(sum % 10)
    a = sum // 10
    p2 = p2.next
    p = p.next
if a == 1:
    p.next = ListNode(a)


