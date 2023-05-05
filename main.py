#task number 1

from collections import deque

steps=0 #make global variable which hold number of steps

def hanoi(n,sour,dest,buff):
    global steps
    steps += 1  #if launch add one more

    if(n==1):
        dest.append(sour.pop())     #from remove to dest add
        print(list(sour), list(buff),list(dest))
    else:
        hanoi(n-1,sour,buff,dest)   #launch hanoi with move -1
        dest.append(sour.pop()) #from remove to dest add
        print(list(sour),list(buff),list(dest))

        hanoi(n-1,buff,dest,sour)

sour = deque([i for i in range(20,0,-1)])    #create queue with number of circles
buff=deque()    #create empty queue
dest=deque()    #create empty queue

print(list(sour),list(buff),list(dest)) #print first look of stack of queues
hanoi(len(sour),sour,dest,buff) #launch hanoi

print("Number of moves: " + str(steps))