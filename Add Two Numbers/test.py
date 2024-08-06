from add_two_numbers import *


# @dataclass
# class ListNode:
#     value: int
#     next: Optional['ListNode'] = None


def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


test1 = {
    "l1": [2, 4, 3],
    "l2": [5, 6, 4],
}

test2 = {
    "l1": [0],
    "l2": [0],
}

test3 = {
    "l1": [9, 9, 9, 9, 9, 9, 9],
    "l2": [9, 9, 9, 9],
}

test_cases = (test1, test2, test3)


for test in test_cases:
    l1_linked_list = list_to_linked_list(test["l1"])
    l2_linked_list = list_to_linked_list(test["l2"])
    res = add_two_numbers(l1_linked_list, l2_linked_list)

    while res is not None:
        print(res.value, end="->")
        res = res.next
    print()

print()
