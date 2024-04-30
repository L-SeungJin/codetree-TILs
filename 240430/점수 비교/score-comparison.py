m=input()
e=input()
arr1=m.split()
arr2=e.split()
A_m=int(arr1[0])
B_m=int(arr2[0])
A_e=int(arr1[1])
B_e=int(arr2[1])

if A_m>B_m and A_e>B_e:
    print('1')
else:
    print('0')