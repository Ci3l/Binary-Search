minput = input()
minput = minput.split(',')
item = input()
item = str(item)
if (item in minput) == False :
    print('error : cannot find your item in your input')
    print('input :', minput)
    print('item :',item)
    item = input()
i = (len(minput))
j = int(i/2)
minput = sorted(minput, key=int)
minput_uncut = list(minput)
print(minput)
index = j
if minput[j] == item :
    print('index ->',j)
while str(minput_uncut[index]) != str(item) :
        j = int(len(minput)/2)
        i = len(minput)
        if int(minput[j]) < int(item) :
            y = [*range(j+1)]
            y.sort(reverse=True)
            z = 0
            while z < len(y) :
                h = y[z]
                del minput[h]
                z = z + 1
            if (isinstance(index, float)) == True :
                index = (index + len(minput)/2) + 0.5
            else :
                index = (index + len(minput)/2) +1
                index = int(index)
        elif int(minput[j]) > int(item) :
            y = [*range(j,i)]
            y.sort(reverse=True)
            z = 0
            while z < len(y) :
                h = y[z]
                del minput[h]
                z = z + 1
            if (isinstance(index, float)) == True :
                index = (index - len(minput)/2) - 0.5
            else :
                index = (index - len(minput)/2)
                index = int(index)
        j = int(len(minput)/2)
        i = len(minput)
        print('>',minput)
        if minput_uncut[int(index)] != minput[j] :
            print('an error occured')
if (minput_uncut[int(index)]) != item :
    print('an error occured')
print('index ->',index)
