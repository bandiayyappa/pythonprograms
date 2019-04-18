# prime numbers
def get_primes(n):  
    primesList = []
    for each in range(2, n + 1):
        isPrime = True
        sqrt = int(each ** 0.5)
        for num in range(2, sqrt + 1):
            if each % num == 0:
                isPrime = False
                break
        if isPrime:
            primesList.append(each)
    
    return primesList
while True:
    n = input('enter number')
    if not n.isdigit():
        print('wrong input given')
        continue
    break
print(get_primes(int(n)))
