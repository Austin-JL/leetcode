# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next : 
            return head  
        p = slow = fast = head
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        p.next = None
        #sort left 
        L = self.sortList(head)
        R = self.sortList(slow)
        return self.sort(L,R)
    
    def sort(self,L,R):
        ans = ListNode(0)
        cur = ans
        while L and R:
            if L.val < R.val:
                cur.next = L
                L = L.next
            else:
                cur.next = R
                R = R.next
                
            cur = cur.next
        cur.next = L or R
        return ans.next