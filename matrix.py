m=int(input())
n=int(input())
matrix=[[0]*n]*m
for i in range(m):
    row=list(map(int, input().split()))
    matrix[i]=row
for i in range(m):
    for j in range(n):
        if i==0 or j==0 or i==m-1 or j==n-1:
            continue
        else:
            matrix[i][j]=0
for i in range(m):
    print(" ".join(str(x) for x in matrix[i]))
