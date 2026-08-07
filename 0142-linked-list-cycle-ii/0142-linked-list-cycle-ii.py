class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Step 2: Find the starting node of the cycle
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr

        return None