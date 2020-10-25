#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #翻转子链表
    def reverse(self, head, tail):
        prev, cur = tail.next, head
        while prev != tail:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return tail, head

    def reverseKGroup(self, head, k):
        hair = ListNode(0)
        hair.next = head
        prev = hair
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail: return hair.next
            nex = tail.next
            head, tail = self.reverse(head,tail)
            prev.next = head
            tail.next = nex

            prev = tail
            head = tail.next
        return hair.next




        
        
# @lc code=end

