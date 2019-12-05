import math
num = input("Enter a number: ")
num = abs(int(num))
r=0
v=0
n = int(math.sqrt(num))
if num < 2:
    print('%d is not prime' % num)
    exit()
if num == 2 or num == 3 or num == 5 or num == 7 or num == 11 or num == 13:
    print('%d is prime' % num)
    exit()
if num % 2 == 0:
    print('%d is not prime' % num)
    exit()
for v in range(3,n,2):
    r = num % v
    if r == 0:
        break
print(' number %d' % num,' remainder %d' % r,'divisor %d' % v, 'square root %d' % n)

if n - v <= 2:
    print('%d is prime' % num)
else:
    print('%d is not prime' % num)
    