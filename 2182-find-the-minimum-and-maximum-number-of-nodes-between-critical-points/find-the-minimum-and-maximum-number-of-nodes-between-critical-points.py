class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_idx = -1
        prev_idx = -1
        min_dist = float("inf")

        prev = head
        curr = head.next
        idx = 1

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (
                curr.val < prev.val and curr.val < curr.next.val
            ):
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx

            prev = curr
            curr = curr.next
            idx += 1

        if min_dist == float("inf"):
            return [-1, -1]

        max_dist = prev_idx - first_idx
        return [min_dist, max_dist]