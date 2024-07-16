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
            
        return head

    def fmtNodes(self):
        head = ListNode(self.val,self.next)
        current = head

        arr = []

        while(current.next):

            arr.append(current.val)
            current = current.next

        arr.append(current.val)



        return arr
        

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

newNode = ListNode(9)
newList = ListNode().convertArray([2,3,4])
print(newList.fmtNodes())