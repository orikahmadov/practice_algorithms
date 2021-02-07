while c <= 10:
    print(c)
    c +=1



while True:
    print(c)
    c +=1
    if c == 11:
        break
    else:
        continue

        
#NESTED LOOPS E.G BUBBLE SORT

list = [10,8,6,5,3,2,1]
for i in range(len(list)- 1):           #outer loop starts from 0 ---> to -1 one before the last item of the list
    for j in range(i + 1, len(list)):   #inner loop! The "inner loop" will be executed one time for each iteration of the "outer loop"
        if list[i] > list[j]:
            list[j],list[i] = list[i], list[j]
 
    
