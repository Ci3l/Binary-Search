input_ = input()
input_ = input_.split(',')
research = input()
research = str(research)
if (research in input_) == False :
    print('error')
i = (len(input_))-1
j = int(i/2)
input_.sort()
print(input_)
result = j
if input_[j] == research :
    print('index',j+1)
while input_[j] != research :
        print('bip bidiboup')
        j = int(len(input_)/2)
        i = len(input_)-1
        if input_[j] < research :
            print(input_[j],'>',research)
            y = [*range(j+1)]
            y.sort(reverse=True)
            print(y)
            z = 0
            while z < len(y) :
                h = y[z]
                del input_[h]
                print('j',j,'i',i)
                print('>',input_,y[z])
                z = z + 1
            result = (result + (len(y)-1))+(len(input_)/2)
        elif input_[j] > research :
            print(input_[j],'>',research)
            y = [*range(j,i+1)]
            y.sort(reverse=True)
            print(y)
            z = 0
            while z < len(y) :
                h = y[z]
                del input_[h]
                print('j',j,'i',i)
                print('>',input_,y[z])
                z = z + 1
            result = result
        j = int(len(input_)/2)
        i = len(input_)-1
print('index',result)
