class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        pos = 1
        first = -1
        last = -1
        min_dist = float('inf')
        while curr.next:
            next_node = curr.next
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):
                if first == -1:
                    first = pos
                if last != -1:
                    min_dist = min(min_dist, pos - last)
                last = pos
            prev = curr
            curr = next_node
            pos += 1
        if first == -1 or first == last:
            return [-1, -1]
        max_dist = last - first
        return [min_dist, max_dist]