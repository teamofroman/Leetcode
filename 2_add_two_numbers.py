from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = None
        cur_elem = None
        prev_elem = None

        hd = 0
        sd = 0

        while l1 is not None or l2 is not None:
            if l1 is not None:
                d1 = l1.val
                l1 = l1.next
            else:
                d1 = 0

            if l2 is not None:
                d2 = l2.val
                l2 = l2.next
            else:
                d2 = 0

            s = d1 + d2 + hd

            hd = s // 10
            sd = s % 10

            cur_elem = ListNode(sd)
            if head is None:
                head = cur_elem
                prev_elem = cur_elem
            else:
                prev_elem.next = cur_elem
                prev_elem = cur_elem

        if hd != 0:
            cur_elem = ListNode(hd)
            if head is None:
                head = cur_elem
                prev_elem = cur_elem
            else:
                prev_elem.next = cur_elem
                prev_elem = cur_elem

        return head


def buid_list(arr: List[int]) -> Optional[ListNode]:
    head = None
    cur_elem = None
    prev_elem = None

    for el in arr:
        cur_elem = ListNode(el)
        if head is None:
            head = cur_elem
            prev_elem = cur_elem
        else:
            prev_elem.next = cur_elem
            prev_elem = cur_elem

    return head


def print_list(list_head: Optional[ListNode]):
    cur_elem = list_head
    while cur_elem is not None:
        print(cur_elem.val, end=' ')
        cur_elem = cur_elem.next
    print()


if __name__ == '__main__':
    nl1 = [9, 9, 9, 9, 9, 9, 9]
    nl2 = [9, 9, 9, 9]

    l1 = buid_list(nl1)
    l2 = buid_list(nl2)

    obj = Solution()

    head = obj.addTwoNumbers(l1, l2)
    print_list(head)
