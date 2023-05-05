#task number 2

from collections import deque

def hanoi(sour,dest,buff):
    steps_iter=0
    if(not len(sour)%2):    #if count of circles is even
        while(True):
            try:
                if(len(sour) and ((not len(buff)) or sour[-1]< buff[-1])): #if sour is not empty and( buff is not empty or last element is sour is smaller then buff
                    buff.append(sour.pop())
                else:
                    sour.append(buff.pop())
                steps_iter+=1
                print(list(sour),list(buff),list(dest))

                if(not len(dest) or sour[-1]<dest[-1]):     #if dest is not empty of last element of sour is smaller then dest
                    dest.append(sour.pop())
                else:
                    sour.append(dest.pop())
                steps_iter+=1
                print(list(sour), list(buff), list(dest))

                if(dest[-1]<buff[-1]):  #if last element of dest is smaller then buff
                    buff.append(dest.pop())
                else:
                    dest.append(buff.pop())
                steps_iter+=1
                print(list(sour), list(buff), list(dest))

            except IndexError: #if out of range break
                break

    else:   #if count of circles is not even
        while(True):
            try:
                if(not len(dest) or sour[-1]<dest[-1]):     #if dest is not empty or last element of sour is smaller then dest
                    dest.append(sour.pop())
                else:
                    sour.append(dest.pop())
                steps_iter+=1
                print(list(sour), list(buff), list(dest))

                if(len(sour) and (not len(buff) or sour[-1]<buff[-1])): #if sour has element and (not empty buff or last element in sour is smaller then buff)
                    buff.append(sour.pop())
                else:
                    sour.append(buff.pop())
                steps_iter+=1
                print(list(sour), list(buff), list(dest))

                if(buff[-1]<dest[-1]):  #if last element in buff is smaller then dest
                    dest.append(buff.pop())
                else:
                    buff.append(dest.pop())
                steps_iter+=1
                print(list(sour), list(buff), list(dest))

            except IndexError:#if out of range break
                break

    return steps_iter       #return number

#main
sour = deque([i for i in range(25,0,-1)])    #create queue with number of circles
buff=deque()    #create empty queue
dest=deque()    #create empty queue

print(list(sour),list(buff),list(dest)) #print first look of stack of queues
steps=hanoi(sour,dest,buff) #launch hanoi
print(list(sour),list(buff),list(dest)) #print last view of hanoi
print("Number of moves: " + str(steps))