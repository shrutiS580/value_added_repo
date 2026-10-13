
n = int(input("Enter your number: "))

if n <= 1:
    print("false")
else:
    for i in range(2, n):
        if n % i == 0:
            print("false")
            break
    else:
        print("true")
