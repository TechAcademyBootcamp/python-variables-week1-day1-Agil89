site_name = input('ENter the domain:')
l = []
for x in range(5):
    page = input('Enter the pages:')
    l.append(page)
print("5 pages tested on",site_name)

for x in l:
    print("tested pages:",x)