from typing import List
class Solution(object):
    matrix = []
    def rotate(self) -> List[List[int]]:
 
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix = self.matrix

      
        LT = [0,0]
        RT = [0,len(matrix)-1]
        RB = [len(matrix)-1,len(matrix)-1]
        LB = [len(matrix)-1,0]

        centered = False
        row = 0

        while(centered == False):
            if(LT == [row,len(matrix)-(1+row)]):
               
                # resets the pointer to continue the incrementing
                LT = [row,row]
                RT = [row,len(matrix)-1]
                RB = [len(matrix)-1,len(matrix)-1]
                LB = [len(matrix)-1,row]

           
                row+= 1
                # moving all 4 pointers inwards a row

                
                RT[0] += row
                RT[1] -= row

                RB[0] -= row
                RB[1] -= row

                LB[0] -= row
                LB[1] += row
               
               
                
            else: # moving numbers use 4 pointers and a swap variable  
                print(centered)
                swp = matrix[LT[0]][LT[1]]
                matrix[LT[0]][LT[1]] = matrix[LB[0]][LB[1]]
                matrix[LB[0]][LB[1]] = matrix[RB[0]][RB[1]]
                matrix[RB[0]][RB[1]] = matrix[RT[0]][RT[1]]
                matrix[RT[0]][RT[1]] = swp

                LT[1] += 1
                RT[0] += 1
                LB[0] -= 1
                RB[1] -= 1


            # this check wether we've centered or not
            if(len(matrix) % 2 == 0):
                print("LT"+str(LT),"RT"+str(RT))
                print("LB"+str(LB),"RB"+str(RB))
            
                if(LT == [len(matrix)/2-1,len(matrix)/2-1]):
                    swp = matrix[LT[0]][LT[1]]
                    matrix[LT[0]][LT[1]] = matrix[LB[0]][LB[1]]
                    matrix[LB[0]][LB[1]] = matrix[RB[0]][RB[1]]
                    matrix[RB[0]][RB[1]] = matrix[RT[0]][RT[1]]
                    matrix[RT[0]][RT[1]] = swp

                    LT[1] += 1
                    RT[0] += 1
                    LB[0] -= 1
                    RB[1] -= 1
            
                    centered = True
            else:
                if(LT == [len(matrix)//2+1,len(matrix)//2+1]):
                   centered = True
            
            print()

        return matrix 
    def __init__(self,matrix):
        self.matrix = matrix
        
m5 = [['01','02','03','04','05'],['06','07','08','09','10'],['11','12','13','14','15'],['16','17','18','19','20'],['21','22','23','24','25'],]
m4 = [['01','02','03','04'],['05','06','07','08'],['09','10','11','12'],['13','14','15','16'],]
m3 = [['01','02','03'],['04','05','06'],['07','08','09'],]
m2 = [['01','02'],['03','04'],]
printMat(Solution(m2).rotate())

#print(Solution(m3).rotate())
#print(Solution(m4).rotate())
#print(Solution(m5).rotate())