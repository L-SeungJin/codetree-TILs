first=input()
second=input()
one=first.split()
two=second.split()
first_age=int(one[0])
first_sex=one[1]
second_age=int(two[0])
second_sex=two[1]
if (first_age>=19 and first_sex=='M') or (second_age>=19 and second_sex=='M'):
    print('1')
else:
    print('0')