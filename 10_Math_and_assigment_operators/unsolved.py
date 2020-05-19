# istifadəçinin doğulduğu ili soruşun və neçə yaşda olduğunu hesablayıb print edin
# ==============================================
a = int(input('enter year of birth'))
now = 2020 -a
print(2020 - a)
# ==============================================

# 2022-ci ildə neçə yaşı olacaq?
# ==============================================
print(2022-a)
then = 2022 -a
# ==============================================
l1= []
l2 = []
# iki rəqəmin ən böyük ortaq bölünənini tapın
# ==============================================
for i in range(1,now +1):
    if now%i==0:
        l1.append(i)
for j in range(1,then+1):
    if then%j==0:
        l2.append(j)
for i in reversed(l1):
    for j in reversed(l2):
        if i==j:
            print(i)
# ==============================================
