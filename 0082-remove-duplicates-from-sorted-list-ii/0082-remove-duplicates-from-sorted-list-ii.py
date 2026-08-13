class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # CHANGE: empty linked list handle karne ke liye
        if not head:
            return head

        duplicates = set()
        temp = head.next
        prev = head

        while temp:
            # CHANGE: head.val ki jagah temp.val compare hoga
            # kyunki adjacent nodes ko compare karke duplicate detect karna hai
            if temp.val == prev.val:
                duplicates.add(temp.val)

            temp = temp.next
            prev = prev.next

        # CHANGE: dummy node add kiya
        # taaki agar head khud duplicate ho, to easily remove ho sake
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