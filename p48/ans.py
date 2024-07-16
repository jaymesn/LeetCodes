from typing import List
def printMat(mat:List[List[int]]):
    for i in range( len(mat)):
        print(mat[i])

class Solution(object):
    matrix = []
    def rotate(self) -> List[List[int]]:
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix = self.matrix
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r-l):
                top,  bottom = l,r
                topl = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topl
            r -=1
            l +=1


        return matrix



    def __init__(self,matrix):
        self.matrix = matrix
m5 = [['01','02','03','04','05'],['06','07','08','09','10'],['11','12','13','14','15'],['16','17','18','19','20'],['21','22','23','24','25'],]
m4 = [['01','02','03','04'],['05','06','07','08'],['09','10','11','12'],['13','14','15','16'],]
m3 = [['01','02','03'],
      ['04','05','06'],
      ['07','08','09'],]

m2 = [['01','02'],['03','04'],]
m1 = [['01']]
printMat(Solution(m5).rotate())
print()
printMat(Solution(m4).rotate())
print()
printMat(Solution(m3).rotate())
print()
printMat(Solution(m2).rotate())
print()
printMat(Solution(m1).rotate())



