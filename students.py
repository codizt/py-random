TEST_CASE=input()
n=int(input()) # Number of students
keys=input().split(",")
students={}
for i in range(1,n+1):
    arr=input().split(",")
    ar=[int(x) for x in arr]
    students[ar[0]]={}
    for j in range(1,len(keys)):
        students[ar[0]][keys[j]]=ar[j]