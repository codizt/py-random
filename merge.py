def merge(D1,D2,priority):
    D={}
    if priority=="first":
        for key, value in D1.items():
            D[key]=value
        for key, value in D2.items():
            if key not in D:
                D[key]=value
    else:
        for key, value in D2:
            D[key]=value
        for key, value in D1:
            if key not in D:
                D[key]=value
    return D

d1={1:1,2:2,3:3,4:4}
d2={4:4,5:5,6:6}
print(merge(d1,d2,"first"))