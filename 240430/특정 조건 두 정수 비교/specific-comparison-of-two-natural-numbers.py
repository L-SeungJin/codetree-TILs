n=input()
arr=n.split()
a=int(arr[0])
b=int(arr[1])
if a<b:
    a=1
    b=0
else:
    a=0
    b=1
print(f'{a} {b}')