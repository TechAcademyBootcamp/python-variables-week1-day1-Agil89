domain = input("enter the domain of the site:")
counter = 0
for x in range(5):
    input("enter the links of 5 pages to be tested:")
    testing_results = int(input('enter 1 for pages with a `successful` test result and 0 for pages with a `failed` test result:'))
    if testing_results == True:
        counter = counter + 1
print('5 pages are tested,',counter, 'of them were succesfull and', 5-counter ,'of them failed')



