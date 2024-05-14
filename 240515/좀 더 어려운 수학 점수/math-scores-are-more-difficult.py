A=input()
B=input()
a=A.split()
b=B.split()
math_a=int(a[0])
eng_a=int(a[1])
math_b=int(b[0])
eng_b=int(b[1])
if math_a>math_b:
    print('A')
else:
    print('B')

if math_a==math_b and eng_a>eng_b:
    print('A')
elif math_a==math_b and eng_a<eng_b:
    print('B')