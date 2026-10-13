n1 = int(input())
n2 = int(input())

a = n1
b = n2

while n2 != 0:
    n1, n2 = n2, n1 % n2

gcd = abs(n1)

if a == 0 or b == 0:
    print(0)
else:
    lcm = abs(a * b) // gcd
    print(lcm)
