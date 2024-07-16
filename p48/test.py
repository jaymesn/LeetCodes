k=0
n=4

exiting = False
while (exiting == False):
    n = int(input("num:"))
    for i in range(n):
        print("[",end="")
        comma2=""
        if(i != n-1): comma2 = ","
        for j in range(n):
            k+=1
            comma = ""
            if(j != n-1): comma = ','

            if(k < 10):
                print("'"+str(0)+str(k)+"'"+comma,end="")
            else:
                print("'"+str(k)+"'"+comma,end="")
        print("],"+comma,)
    n=0