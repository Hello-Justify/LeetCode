'''
2.两数相加
@author   : hca
@date     : 2019-11-17 22:00
@parameter: 
    {
    l1:被加数链表
    l2:加数链表
    }
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 构建链表
def build(nums):
    fina = ListNode(0)
    pointer = fina
    for num in nums:
        pointer.next = ListNode(num)
        pointer = pointer.next
    return fina.next

# 显示链表
def abolish(list_node):
    l = []
    while(list_node):
        l.append(list_node.val)
        list_node = list_node.next
    print(l)

# 两数之和
def addTwoNumbers(l1, l2) -> ListNode:
    fina = ListNode(0)
    pointer = fina
    cf = 0
    while(1):
        if (l1 is None) and (l2 is None) and (cf == 0):
            break
        pointer.next = ListNode(cf)
        pointer = pointer.next
        if l1:
            pointer.val += l1.val
            l1 = l1.next
        if l2:
            pointer.val += l2.val
            l2 = l2.next
        cf = pointer.val // 10
        pointer.val = pointer.val % 10
    return fina.next

if __name__ == '__main__':
    l1 = build([5])
    l2 = build([5,3,2])
    ob = addTwoNumbers(l1, l2)
    abolish(ob)