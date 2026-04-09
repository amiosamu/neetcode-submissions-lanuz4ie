class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            next_node = curr.next
            gcd = math.gcd(curr.val, next_node.val)

            new_node = ListNode(gcd)
            new_node.next = next_node
            curr.next = new_node

            curr = next_node
        return head
