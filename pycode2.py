import random

heads = [88,135,192,152]

hits = [25,67,1,62]
growths = [15,25,15,34]



def dragon_killing():
    
    iter_limit = 1000

    for head in heads:
        iters = 0           #Resets iters at every new 'dragon'
        while head != 0:
            iters += 1

            if iters == iter_limit:
                print("NO")             #Does not mean that dragon is necessarily unkillable
                break
            else:
                i = random.randint(0,3) #Randomly choose a hit value
                if head >= hits[i]:
                    head -= hits[i]

                    if head == 0:
                        print(f'''
YES...............................................{iters}


''')
                    else:
                        head += growths[i]
                        print(head, hits[i], growths[i], iters)
                else:
                    iters -= 1

dragon_killing()
                    
                
            
