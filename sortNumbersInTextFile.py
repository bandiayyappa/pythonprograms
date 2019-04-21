# sort numbers in a text file

fh = open('numbers.txt','r')
data = fh.read().strip().split()
fh.close()
data = list(map(int,data))
data.sort()
str_data = list(map(str,data))
str_data = ' '.join(str_data)
fh = open('output.txt','w')
fh.write(str_data)
fh.close()
