n=input()
arr=n.split()
a=int(arr[0])
b=int(arr[1])
a+=b
b+=a
print(f"{a} {b}")