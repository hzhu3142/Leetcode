class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        p = head
        
        while p:
            if not p.child:
                p = p.next
            else:
                q = p.child
                while q.next:
                    q = q.next
                q.next = p.next
                if p.next:
                    p.next.prev = q
                p.next = p.child
                p.next.prev = p
                p.child = None
        
        return head
