class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        duplicates = set()
        temp = head.next
        prev = head

        while temp:
            if temp.val == prev.val:
                duplicates.add(temp.val)
            temp = temp.next
            prev = prev.next

        if head.val in duplicates:
            head = head.next
            while head and head.val in duplicates:
                head = head.next

        prev = head

        if not prev:
            return None

        temp = head.next

        while temp:
            if temp.val not in duplicates:
                prev.next = temp
                prev = prev.next
            temp = temp.next

        prev.next = None

        return head