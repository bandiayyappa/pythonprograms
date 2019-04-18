# Linear search
num = input('enter numbers followed by space').strip().split()
def hasNum(n):
    if n.isdigit():
        return True
    return False
numList = list(filter(hasNum,num))
numList = list(map(int,numList))

def linear(numList):
    findNum = int(input("give a number you want to find "))
    hasNum = False
    position = 0
    while position < len(numList):
        if numList[position] == findNum:
            return True,position,findNum
        position = position + 1

    return hasNum,'Not found',findNum


hasNum,message,findNum = linear(numList)
if hasNum:
    print('number',findNum,'available in the',message+1,'position')
else:
    print("given number",findNum,'not available in list')
