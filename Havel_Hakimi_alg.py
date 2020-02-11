list = [14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]
copy = list
while True:
    while 0 in list:
        list.remove(0)

    if len(copy) == 0:
        print("True")
        break

    copy.sort(reverse = True)
    print(copy)

    N = copy[0]
    x = 0
    copy.remove(copy[0])

    if N > len(copy):
        print("false")
        break
    else:
        while x < N:
            num = copy[x]
            num = num - 1
            copy[x] = num
            x += 1

