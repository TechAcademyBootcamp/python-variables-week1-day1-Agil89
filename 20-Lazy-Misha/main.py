t1 = int(input('t1 time:'))
while t1<1 or t1>1000:
    print('enter the number between 1 and 1000')
    t1 = int(input('t1 time:'))
t2 = int(input('t2 time:'))
while t2<1 or t2>1000:
    print('enter the number between 1 and 1000')
    t2 = int(input('t2 time:'))
t3 = int(input('t3 time:'))
while t3<1 or t3>1000:
    print('enter the number between 1 and 1000')
    t3 = int(input('t3 time:'))
if t1<t2 and t1<t3:
    print(t1)
elif t2<t1 and t2<t3:
    print(t2)
else:
    print(t3)