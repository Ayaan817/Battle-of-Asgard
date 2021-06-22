import random

n = [88,135,192,152]
iters = 0

hits = [25,67,1,62]
growths = [15,25,15,34]

for x in n:
    while x != 0:
        i = random.randint(0,3)
        iters += 1
        if iters == 100000:
            print("No")
            break
        else:
            if x >= hits[i]:
                x -= hits[i]
            
                if x == 0:
                    print("Yes",iters)
                    print("______________________________________________________________________________________________________________________________________________________")
                    
                else:
                    x += growths[i]
                    
