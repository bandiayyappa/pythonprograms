# Binary search
myList = [ 1,10,9,20,2,300 ]
value = 10

def binary_search (myList, L, r, value):
        myList.sort()
        if r >= L:
                middle = L + int((r - L)/2)
                if myList[middle] == value:
                        return middle
                elif myList[middle] > value:
                        return binary_search(myList, L, middle-1, value)
                else:
                        return binary_search(myList, middle + 1, r, value)
        else:return None


position = binary_search(myList, 0, len(myList)-1, value) 

if position != None: 
	print('the value ',value,'found in index',position )
else: 
	print("Value",value,'not found ')
