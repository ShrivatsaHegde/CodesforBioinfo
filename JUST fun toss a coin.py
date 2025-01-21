import sleep
head=0
tail=0
flip=int(input("how many coin toss todo:"))
for i in range(flip):
    result=raudint(0,1)
    sleep(1)
    if result==0:
        print ("heads")
        heads+=1
    elif:
        print("tails")
        tail+=1

print("the results are:")  
print("heads",head)
print("tail",tail)  