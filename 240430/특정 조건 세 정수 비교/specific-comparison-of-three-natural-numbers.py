n=input()
arr=n.split()
n1=int(arr[0])
n2=int(arr[1])
n3=int(arr[2])

if n1==min(arr):
    print('1',end=" ")
else:
    print('0',end=" ")
if n1==n2 and n2==n3:
    print('1')
else:
    print('0')