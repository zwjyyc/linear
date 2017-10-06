class TestClass(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head_node):
    cur_node = head_node.next.next
    pre_node = head_node.next

    pre_node.next = None

    while cur_node.next:
        next_node = cur_node.next
        cur_node.next = pre_node
        pre_node = cur_node
        cur_node = next_node

    cur_node.next = pre_node
    return cur_node

pHead = TestClass(-1)

preNode = pHead

for i in range(0, 20):
    curNode = TestClass(i)
    preNode.next = curNode
    preNode = preNode.next

curNode = pHead
while curNode.next != None:
    curNode = curNode.next
    print str(curNode.value) + '#'

curNode = reverse(pHead)

print str(curNode.value) + '#'

cnt = 0
while curNode.next:
    curNode = curNode.next
    print str(curNode.value) + '#'
    if cnt > 10:
        break
    cnt += 1

