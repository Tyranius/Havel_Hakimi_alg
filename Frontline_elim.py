#Number of entries to subtract 1 from
N = 1

list = [1]
x = 0
copy = list
while x < N:
    num = copy[x]
    num = num - 1
    copy[x] = num
    #print(num)
    x +=1
print(copy)