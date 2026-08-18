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
B=input_matrix()

print("Matrix A:",A)
print("Matrix B:",B)
#matrix multiply
def multiply(A,B):
   if len(A[0])!=len(B):
         print("matrix multiplpy not possible")
         return None
   C=[]
   for i in range(len(A)):
         
         row=[]
         for j in range(len(B[0])):
             output=0
             for k in range(len (B)):
                 
                 output+=A[i][k]*B[k][j]

             row.append(output)
         C.append(row)
   return C
C=multiply(A,B)
if C !=None:
     print("Multiplication of A and B:")
     for row in C:
         print(row)