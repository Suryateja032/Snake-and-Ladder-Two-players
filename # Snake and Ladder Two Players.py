# Snake and Ladder Two Players
import random
sandl={95:5,80:20,46:21,38:26,57:25,65:15,70:18,62:9,73:24}
def issafe(sl,newpos):
    if newpos in sl:
        p=sl[newpos]
        print("you have been bitten by a snake")
        return p
    elif newpos in sl.values():
        print("you have stepped in ladder")
        for i in sl:
            if sl[i]==newpos:
                p=i
                return p
    else:
        return newpos
def printboard(sandl,pos,pos2):
    l=list(sandl.values())  
    for row in range(10,0,-1):
        for col in range(1,11):
            num=row*10-col
            if num==pos:
                print("[p]",end=" ") 
            elif num==pos2:
                print("[p2]",end=" ")
            elif num in sandl:
                print("[s]",end=" ")
            elif num in l:
                print("[l]",end=" ")
            else:
                print("[ ]",end=" ") 
        print()
 
 
 
 
pos=0
pos2=0
printboard(sandl,pos,pos2)
def rand():
    return random.randint(1,6)
curr=pos
while pos<100:
  if curr==pos:
    print("your player1 is in",pos)
    input("press Enter to play")
    newno=rand()
    print("your lucky no is in",newno)
    print(""*20)
    pos=pos+newno
    new=issafe(sandl,pos)
    pos=new
    printboard(sandl,pos,pos2)
    print("your new position is ",pos)
    print("_"*20)
    print("_"*20)
    curr=pos2
  else:
    print("your player 2 is in",pos2)
    input("press Enter to play")
    newno=rand()
    print("your lucky no is in",newno)
    print(""*20)
    pos2=pos+newno
    new=issafe(sandl,pos2)
    pos2=new
    printboard(sandl,pos,pos2)
    print("your new position is ",pos2)
    print("_"*20)
    print("_"*20)
    curr=pos
print("congrats you won the game")
