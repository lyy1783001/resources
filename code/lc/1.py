# 1:56
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def list2LinkList(nums:list[int])->LinkNode:
    dummy = LinkNode(-1)
    p = dummy
    for i in range(len(nums)):
        cur_node = LinkNode(nums[i])
        p.next = cur_node
        p = cur_node
    return dummy.next

nums = [1,2]
head = list2LinkList(nums)

def reverseList(head:LinkNode):
    if not head.next:
        return head
    p = head
    rever_head = reverseList(p.next)
    p.next.next = p
    p.next = None
    return rever_head

p = head
n = 0
while p:
    p = p.next
    n += 1
print(n)
if n%2 == 0:
    k = n // 2
else:
    k = n // 2 +1
p1 = head
for _ in range(k):
    p1 = p1.next

p1 = reverseList(p1)
p2 = head
while p1:
    if p1.val != p2.val:
        print(False)
    p1=p1.next
    p2=p2.next
