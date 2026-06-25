# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            # 使用 math.gcd 函数计算最大公约数
            common_val = math.gcd(curr.val, curr.next.val)
            
            # 创建新节点
            new_node = ListNode(common_val)
            
            # 插入新节点
            new_node.next = curr.next
            curr.next = new_node
            
            # 移动指针到原来的下一个节点
            curr = new_node.next
            
        return head