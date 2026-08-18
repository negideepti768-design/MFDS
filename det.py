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
def deter(A):
     n =len(A)
     for row in A:
         if len(row)!= n:
             print("Determinant is possible only for a square matrix.")
             return None
     if n==1:
         return A[0][0]
     if n==2:
         return A[0][0]*A[1][1] -A[0][1]*A[1][0]
     det=0
     for j in range(n):
         minor=[]
         for i in range(1,n):
             row =[]
             for k in range(n):
                 if k!=j:
                     row.append(A[i][k])

             minor.append(row)
         det = det+((-1)** j)*A[0][j]*deter(minor)
     return det        
D = deter(A)

if D !=None:
     print("Determinant of A:", D)