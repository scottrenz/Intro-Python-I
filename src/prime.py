num = input("Enter a number: ")
num = abs(int(num))
r=0
v=0
for v in range(2,num):
    r = num % v
    if r == 0:
        break
print(num,r,v)

if v == num -1 or (r == 0 and v == 0):
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')
    