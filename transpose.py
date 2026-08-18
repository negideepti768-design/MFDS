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
#Transpose of matrix
def transpose(A):
     T=[]
     for j in range(len(A[0])):
         row=[]
         for i in range(len(A)):
             row.append(A[i][j])
         T.append(row)

     return T
T=transpose(A)
print("Transpose of A:")
for row in T:
     print(row)