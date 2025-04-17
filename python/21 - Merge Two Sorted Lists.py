class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    new_list = ListNode()
    head = new_list
    while list1 or list2:
        if list2 is None or (list1 and list1.val <= list2.val):
            new_list.next = list1
            list1, new_list = list1.next, list1
        else:
            new_list.next = list2
            list2, new_list = list2.next, list2
            
    return head.next