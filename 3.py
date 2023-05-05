#task number 3

from collections import deque
import time

steps_re=0
steps_it=0

def hanoi_re(n,sour,dest,buff):
    global steps_re
    steps_re+=1
    if(n==1):
        dest.append(sour.pop())     #from remove to dest add
    else:
        hanoi_re(n-1,sour,buff,dest)   #launch hanoi with move -1
        dest.append(sour.pop()) #from remove to dest add

        hanoi_re(n-1,buff,dest,sour)

def hanoi_it(sour,dest,buff):
    global steps_it
    if(not len(sour)%2):
        while(True):
            try:
                if(len(sour) and ((not len(buff)) or sour[-1]< buff[-1])):
                    buff.append(sour.pop())
                else:
                    sour.append(buff.pop())
                steps_it+=1

                if(not len(dest) or sour[-1]<dest[-1]):
                    dest.append(sour.pop())
                else:
                    sour.append(dest.pop())
                steps_it+=1

                if(dest[-1]<buff[-1]):
                    buff.append(dest.pop())
                else:
                    dest.append(buff.pop())
                steps_it+=1

            except IndexError:
                break
    else:
        while(True):
            try:
                if(not len(dest) or sour[-1]<dest[-1]):
                    dest.append(sour.pop())
                else:
                    sour.append(dest.pop())
                steps_it+=1

                if(len(sour) and (not len(buff) or sour[-1]<buff[-1])):
                    buff.append(sour.pop())
                else:
                    sour.append(buff.pop())
                steps_it+=1

                if(buff[-1]<dest[-1]):
                    dest.append(buff.pop())
                else:
                    buff.append(dest.pop())
                steps_it+=1

            except IndexError:
                break

sour_1 = deque([i for i in range(23,0,-1)])    #create queue with number of circles
buff_1=deque()    #create empty queue
dest_1=deque()    #create empty queue
z1=time.time()
hanoi_re(len(sour_1),sour_1,dest_1,buff_1) #launch hanoi
print("Time in recurension: ", time.time()-z1, " Make moves: ", str(steps_re))
sour_2 = deque([i for i in range(23,0,-1)])    #create queue with number of circles
buff_2=deque()    #create empty queue
dest_2=deque()    #create empty queue
z2=time.time()
hanoi_it(sour_2,dest_2,buff_2)
print("Time in iteration: ", time.time()-z2, " Make moves: ", str(steps_it))
