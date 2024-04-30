n=input()
arr=n.split()
n1=int(arr[0])
n2=int(arr[1])
n3=int(arr[2])
if n1<=n2 and n1<=n3:
    print(n1)
elif n2<=n1 and n2<=n3:
    print(n2)
else:
    print(n3)