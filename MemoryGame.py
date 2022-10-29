
import random 

def MemoryGame(n):
    if n%2==0:
        N=n*n
        count=N/2
    else:
        N=n*n
        N=N+1
        count=N/2
    char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","#", "*", "£", "$", "+", "-", "."]
    list=[]
    while(count>0):
        value= char[random.randint(0, len(char) - 1)]
        if value not in list:
            list.append(value)
            count-=1
    if n%2==0:
        list2=list
        list+=list2
    else:
        list2=list[1:]
        list+=list2
    for i in range(n):
        for j in range(n):
            value= list[random.randint(0, len(list) - 1)]
            list.remove(value)
            print(value,end=" ")
        print()


MemoryGame(int(input("Enter the value of n: ")))
