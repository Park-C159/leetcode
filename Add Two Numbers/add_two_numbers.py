from typing import Optional, List
from dataclasses import dataclass

@dataclass
class ListNode:
    value: int
    next: Optional['ListNode'] = None


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(0)
    curr = head
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        val1 = l1.value if l1 is not None else 0
        val2 = l2.value if l2 is not None else 0

        total = val1 + val2 + carry
        if val1 + val2 + carry >= 10:
            val = total % 10
            carry = 1
        else:
            val = total
            carry = 0
        curr.next = ListNode(val)
        curr = curr.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    return head.next