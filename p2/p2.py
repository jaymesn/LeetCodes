# boilerplate linkedList class for my local python implementation
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    def convertArray(self,array=[0]):
        head = ListNode(array[0])
        prev = head

        for i in range(1,len(array)):

            current = ListNode(array[i])
            prev.next = current
            prev = current

        self.val = head.val
        self.next = head.next

        return self


    def fmtNodes(self):
        head = ListNode(self.val,self.next)
        current = head

        arr = []

        while(current.next):

            arr.append(current.val)
            current = current.next

        arr.append(current.val)


        print(arr)
        
        return self

class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """    
        carry = 0
        head = ListNode()
        cur = head

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit calculated and inserted
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update the ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
             
            
            

#ksdfjsldj




tests = [ 
    [[2,4,3],[5,6,4]],
    [[0],[0]],
    [[9,9,9,9,9,9,9],[9,9,9,9]]
]
solution = Solution().addTwoNumbers

for item in tests:
    solution(
        ListNode().convertArray(item[0]),
        ListNode().convertArray(item[1])
    ).fmtNodes()

    

'''
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''
