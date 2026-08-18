def input_matrix():
    r=int(input("Enter no. of rows:"))
    c=int(input("Enter no. of cols:"))
    A=[]
    print("Enter matrix elements:")
    for i in range(r):
            row=list(map(int,input().split()))
            A.append(row)
    return A
A=input_matrix()
print("Matrix A:",A)
#Trace of matrix
def trace(A):
     
     if len(A)!=len(A[0]):
         print("Invalid!Input square matrix for trace")
         return None
     trace=0
     for i in range(len(A)):
         trace=trace+A[i][i]

     return trace
T=trace(A)
if T !=None:
   print("Trace of A:",T)
