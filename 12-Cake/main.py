r = int(input('enter the radius:'))
w = int(input('enter the width:'))
l = int(input('enter the length:'))

h = (w/2)**2+(l/2)**2
r = r**2

if r>h:
    print('YES')
else:
    print('NO')