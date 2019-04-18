# minimum,maximum and average of n numbers
while True:
    n = input('how many numbers you give?')
    if not n.isdigit():
        print('wrong data')
        continue
    break
myList = []
for each in range(int(n)):
    num = input('enter number')
    if (not num.isdigit()) :
        if (num[0]!="-"):
            if len(num)>=2:
                if not num[1:].isdigit():
                    print('wrong input ')
                    continue
    if num[0] == '-':
        if not num[1:].isdigit():
            print('wrong input2')
            continue
        myList.append(-int(num[1:]))
    else:
        myList.append(int(num))
print('minimum of ',myList,' is ',min(myList))
print('maximum of ',myList,' is ',max(myList))
print('average of ',myList,' is ',sum(myList)/len(myList))
