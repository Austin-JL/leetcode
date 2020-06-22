# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        ans = ListNode(0)
        ans.next = head
        
        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                tmp = ans
                node = head.next
                
                while tmp.next.val < node.val:
                    tmp = tmp.next
                # 
                head.next = node.next
                #
                tmp.next, node.next = node,tmp.next
                
        return ans.next