a=[3,3,1,0,2,0,0,1]
point=a[0]
sublist=a
check=0

while check!=(len(a)-1):
    if (check+1)-(a[check]+check+1)==0:
        break
    if point<=(len(a)-1)-(sublist.index(point)):
        sublist=a[check+1:a[check]+check+1]
        point=max(sublist)
        check=sublist.index(point)+check+1
    elif point>(len(a)-1)-(sublist.index(point)):
        check=(len(a)-1)

    print(point)




if check==len(a)-1:
    print("solved")
else:
    print("error")

"""
a=[2,4,1,1,0,2,3]
s=a[1:4]
print(max(s))"""