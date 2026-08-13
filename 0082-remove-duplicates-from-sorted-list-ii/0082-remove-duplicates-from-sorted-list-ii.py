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

        
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        temp = head

        while temp:
            if temp.val not in duplicates:
                prev.next = temp
                prev = prev.next

            temp = temp.next
        prev.next = None
        return dummy.next