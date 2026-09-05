class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# Linked List: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Reverse
new_head = reverseList(head)

# Print
curr = new_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

print("None")