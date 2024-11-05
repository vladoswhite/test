#3

"""v=-1
shows=["ходячие мервтецы","красавцы","уебки","Дневник вампира"]
for i in range(1,5):
    print(i)
    
    v=v+1
    print(shows[v])"""      

#4
"""for n in range(25,51):
        print(n)

while True:
    
    A=input("Отгадай число или нажмите ! для выхода: ")
    A=int(A)
    if A==1:
        print("Вы угадали!")
        break
    if A=="!":
         break"""
   
#5

list1=[8,19,148,4]
list2=[9,1,33,83]
list3=[]

for i in list1:
    for j in list2:
        mult=i*j
        list3.append(mult)
print(list3)



