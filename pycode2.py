import random

heads = [88,135,192,152]

hits = [25,67,1,62]
growths = [15,25,15,34]



def dragon_killing():
    iters = 0
    iter_limit = 1000
    for head in heads:
        while head != 0:
            iters += 1

            if iters == iter_limit:
                print("NO")
                break
            else:
                i = random.randint(0,3)
                if head >= hits[i]:
                    head -= hits[i]

                    if head == 0:
                        print(f'''
YES...............................................{iters}


''')
                    else:
                        head += growths[i]
                        print(head, hits[i], growths[i])
                else:
                    iters -= 1

dragon_killing()
                    
                
            
