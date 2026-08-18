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

#matrixz addition
def addition(A,B):
    C=[]

    for i in range(len(A)):
        row= []
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
            
        C.append(row)
    return C    

C=addition(A,B)
print("Addition of A and B:")
for row in C:
    print(row)

#Matrix subtraction
def subtraction(A,B):
  C=[]

  for i in range(len(A)):
    row= []
    for j in range(len(A[0])):
        row.append(A[i][j]-B[i][j])   

        C.append(row)
    return C   
C=subtraction(A,B)
print("Subtraction of A and B:")
for row in C:
    print(row)

