# Perfect Number or Not
num = int(input(" Enter number"))
total = 0
for i in range(1, num):
    if(num % i == 0):
        total += i
if total == num:
    print(" {} is a perfect number".format(num))
else:
    print(" {} not a perfect number".format(num))
