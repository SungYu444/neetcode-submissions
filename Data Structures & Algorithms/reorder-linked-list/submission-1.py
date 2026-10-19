class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next

        left = 0
        right = len(nodes) - 1

        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None