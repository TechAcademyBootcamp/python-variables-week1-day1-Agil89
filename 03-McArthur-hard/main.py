print('This is a puzzle favored by Gen. MacArthur. Lets start')
birth_month = input('enter your birth month:')
while birth_month.isdigit()==False or (int(birth_month)>12 or int(birth_month)<1):
    print('enter the number between 1 and 12')
    birth_month = input('enter your birth month:')
    continue

age = input('enter your age:')
while age.isdigit()==False:
    print('enter the number ')
    age = input('enter your age:')
    continue

special_number = (((2*int(birth_month)+5)*50) + int(age)) - 365
print(special_number)
answer = special_number + 115
print(answer//100,answer%100)


