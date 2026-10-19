class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        nodes = []

        end = head
        while end is not None:
            nodes.append(end)
            end = end.next

        left = 0
        right = len(nodes) - 1

        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None