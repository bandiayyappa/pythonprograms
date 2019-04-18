# Fibonacci series

while True:
    n = input('enter how many numbers required')
    if (not n.isdigit()) or (n.strip()=="0") :
        print('wrong data given try')
        continue
    elif int(n)<=0:
        print('value should greater than 0')
        continue
    break

def fibonacci(n):
    series = []
    n = int(n)
    if n== 0:
        return series
    elif n == 1:
        series.append(0)
        return series
    else:
        series.append(0)
        series.append(1)
        temp = 3
        while n >= temp:
            temp += 1
            series.append(series[-1]+series[-2])
            
        return series
print(fibonacci(n))
        
    
