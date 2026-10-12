n = int(input("enter your number: "))
count = 0
if n == 0 :
    count = 1
   
else:
    while n > 0:
        digit = n%10
        if digit % 2 != 0:
            count +=1
        n =n//10    
    print("your num of not odd" , count)    

