category = input("Enter your category code:")
beginning = int(input('Enter beginning meter reading:'))
ending = int(input('Enter ending meter reading:'))

def forR(x,y):
    if (y - x) < 0:
        tachometer = 1000000000 + (y-x)
    else:
        tachometer = (y - x) / 10
    sum = 5 + tachometer*0.0005
    return tachometer,round(sum,2)

def forC(x,y):
    if (y - x) < 0:
        tachometer = 1000000000 + (y-x)
    else:
        tachometer = (y - x)/10
    if tachometer>4000000:
        sum = 1000 + (tachometer-4000000) * 0.00025
    else:
        sum = 1000
    return tachometer/10,sum

def forI(x,y):
    if (y - x) < 0:
        tachometer = 1000000000 + (y-x)
    else:
        tachometer = (y - x) / 10
    if tachometer<10000000:
        sum = 2000
    elif tachometer<4000000:
        sum = 1000
    else:
        sum = 3000 + (tachometer - 10000000)*0.00025
    return tachometer/10,sum
if category.lower() == 'r':
    print('Customer code: r')
    print('Beginning meter reading:',beginning)
    print('Ending meter reading:',ending)
    print('Gallons of water used:',forR(beginning,ending)[0])
    print('Amount billed:',forR(beginning,ending)[1])
elif category.lower() == 'c':
    print('Customer code: c')
    print('Beginning meter reading:', beginning)
    print(('Ending meter reading:', ending))
    print('Gallons of water used:', forC(beginning, ending)[0])
    print('Amount billed:', forC(beginning, ending)[1])
elif category.lower() == 'i':
    print('Customer code: i')
    print('Beginning meter reading:', beginning)
    print(('Ending meter reading:', ending))
    print('Gallons of water used:', forI(beginning, ending)[0])
    print('Amount billed:', forI(beginning, ending)[1])