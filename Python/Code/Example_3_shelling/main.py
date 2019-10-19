import random

def happy(arr, ii, jj, counter, zhach):
    for count in range(ii - 1, ii + 2):
        for count1 in range(jj - 1, jj + 2):
            # print("u", arr[count][count1])
            if arr[count][count1] == zhach:
                counter = counter + 1 
                # print("arr", arr[count][count1])
	            # print(counter) 
    if counter > 2:
        # print("happy")
        return 1
    else:
        # print("not happy")
        return 0

def swap(ar):
    n = len(ar)
    for row in ar:
        print(' '.join([str(elem) for elem in row]))
        
    counter = int(0)
    g = random.randint(1, n - 2)
    h = random.randint(1, n - 2)
    while (ar[g][h] == 0) or (happy(ar, g, h, counter, ar[g][h]) == 1):
        counter = 0
        # print("is happy", g, h, ar[g][h])
        g = random.randint(1, n - 2)
        h = random.randint(1, n - 2)
    else:
        # print("not happy is", g, h, ar[g][h])
        swapznach = ar[g][h]
        swapg = g
        swaph = h
        # print("swap", swapznach, swapg, swaph)
	
    while (ar[g][h] != 0 or happy(ar, g, h, counter, swapznach) != 1):
        #print("yx", g, h)
        g = random.randint(1, n - 2)
        h = random.randint(1, n - 2)
        #print("no swap")
    else:
        #print("swap ar  ", ar[g][h], g, h)
        swap = ar[g][h]
        ar[g][h] = swapznach
        ar[swapg][swaph] = swap
        # print("swap", swap)
        # for row in ar:
            # print(' '.join([str(elem) for elem in row]))

def main():
    print("enter N")
    n = int(input())
    a = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = random.randint(0, 100)
            if a[i][j] - 90 > 0: # probability 45%
                a[i][j] = 0
            else: 
                a[i][j] = random.randint(1, 2)
    cc = int(0)
    while 1:
        cc += 1
        print(cc)
        swap(a)

if __name__ == "__main__":
    main()