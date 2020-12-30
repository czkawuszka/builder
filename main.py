#autobuilder by czkawuszka uwuowo
import numpy as np
import time
print("Creating table...")
print(" ")


len=50
len2=25
hash_materials=0   #build

cord = [['-' for x in range(len)] for y in range(len2)]

print("Table created!")

player='o'
posy = 0
posx = 0
cord[posy][posx]=player
painting='n'
erasing='n'
temp2='-'
set_resupply='false'
resupply_pos=[len2-1,len-1]
target=[0,0]

def printarray():
    global len2, len, cord2
    y=0
    x=0
    while(y<len2):
        while(x<len):
            print(cord[y][x], end='')
            x+=1
        x=0
        y+=1
        print(" ")

def help():
    print("Commands:")

    print(" Movement:")
    print("  - right/r - moves one space to the right")
    print("  - left/l - moves one space to the left")
    print("  - up/u - moves one space up")
    print("  - down/d - moves one space down")

    print(" Actions:")
    print("  - paint - starts painting")
    print("  - erase - starts erasing")
    print("  - stop - stops current action")
    print("  - Note: erasing and painting cancel eachother out")
    print("  - exit - exits the program")
    print("  - help - brings out this menu")
    print(" ")
    input("Press any key to continue...")

def auto_move(def_input):
    global posx
    global posy
    global temp, temp2, cord, player
    x=0
    target=[0,0]
    target[0]=def_input[0]
    target[1]=def_input[1]
    print("Target: "+str(target[0])+", "+str(target[1]))
    print("Position: "+str(posy)+", "+str(posx))
    if(posy<target[0]):
        posy+=1
        temp=cord[posy][posx]
        cord[posy][posx]=player
        cord[posy-1][posx]=temp2
    elif(posy>target[0]):
        posy-=1
        temp=cord[posy][posx]
        cord[posy][posx]=player
        cord[posy+1][posx]=temp2
    elif(posx<target[1]):
        posx+=1
        temp=cord[posy][posx]
        cord[posy][posx]=player
        cord[posy][posx-1]=temp2
    elif(posx>target[1]):
        posx-=1
        temp=cord[posy][posx]
        cord[posy][posx]=player
        cord[posy][posx+1]=temp2
    else:
        print("Target Reached!")
        x=1
    return x


help()
while True:
    printarray()

    p_input=str(input('Command: '))
    if(p_input=='up' or p_input=='u'):
        if(posy==0):
            print("You're already at the top end of the space")
        else:
            posy-=1
            temp=cord[posy][posx]
            cord[posy][posx]=player
            cord[posy+1][posx]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
                hash_materials+=1#build
            elif(temp=='#' and erasing=='y'):
                temp2='-'
                hash_materials-=1#build
            else:
                temp2=temp
    elif(p_input=='down' or p_input=='d'):
        if(posy==len2-1):
            print("You're already at the bottom end of the space")
        else:
            posy+=1
            temp=cord[posy][posx]
            cord[posy][posx]=player
            cord[posy-1][posx]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
                hash_materials+=1#build
            elif(temp=='#' and erasing=='y'):
                temp2='-'
                hash_materials-=1#build
            else:
                temp2=temp
    elif(p_input=='left' or p_input=='l'):
        if(posx==0):
            print("You're already at the left end of the space")
        else:
            posx-=1
            temp=cord[posy][posx]
            cord[posy][posx]=player
            cord[posy][posx+1]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
                hash_materials+=1#build
            elif(temp=='#' and erasing=='y'):
                temp2='-'
                hash_materials-=1#build
            else:
                temp2=temp
    elif(p_input=='right' or p_input=='r'):
        if(posx==len-1):
            print("You're already at the right end of the space")
        else:
            posx+=1
            temp=cord[posy][posx]
            cord[posy][posx]=player
            cord[posy][posx-1]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
                hash_materials+=1#build
            elif(temp!='-' and erasing=='y'):
                temp2='-'
                hash_materials-=1#build
            else:
                temp2=temp
    elif(p_input=='pos'):
        print('y= '+str(posy)+' x= '+str(posx))
    elif(p_input=='exit'):
        break
    elif(p_input=='paint'):
        painting='y'
        temp2='#'
        hash_materials+=1
        erasing='n'
    elif(p_input=='stop'):
        painting='n'
        erasing='n'
    elif(p_input=='erase'):
        if(hash_materials==0):
            print("There's nothing to erase!")
        else:
            erasing='y'
            hash_materials-=1
            painting='n'
            temp2='-'
    elif(p_input=='help'):
        help()


    #----------------- build start


    elif(p_input=='build'):
        print("///////////////////////////////")
        print("You chose: build")
        print("Warning! This action cant be undone!")
        print("Confirm? y/n...")
        while True:
            build_input=str(input())
            if(build_input=='y'):
                print("TEMP2:"+temp2)
                cord[posy][posx]=temp2
                temp2='-'
                posy=0
                posx=0
                print("Starting build!")
                print("Materials needed: "+ str(hash_materials)+"# ")
                print("Locating build...")
                build_cords = [[0 for x in range(2)] for y in range(hash_materials)]
                y=0
                x=0
                build_x=0
                print(build_cords)
                while(y<len2):
                    while(x<len):
                        if(cord[y][x]=='#'):
                            print("# FOUND bx= "+str(build_x)+" y="+str(y)+" x="+str(x))
                            build_cords[build_x][0]=y
                            build_cords[build_x][1]=x
                            build_x+=1
                        if(cord[y][x]=='@'):
                            print("@ FOUND"+" y="+str(y)+" x="+str(x))
                        x+=1
                    y+=1
                    x=0
                print("Build found!")
                print(build_cords)
                break
            elif(build_input=='n'):
                print("Why did you type build then?")
                break
            else:
                print("Wrong input! Try again.")
            break

        print("///////////////////////////////")
        print("time to build")
        while True:
            while True:
                printarray()
                z=auto_move(resupply_pos)
                time.sleep(1)
                if(z==1):
                    break
            tempcord=[0,0]
            while True:
                printarray()
                z=auto_move(tempcord)
                time.sleep(1)
                if(z==1):
                    break
            break


    elif(p_input=='set_resupply'):
        temp2="@"

        if(set_resupply=='true'):
            cord[int(resupply_pos[0])][int(resupply_pos[1])]='-'
        else:
            set_resupply='true'
        resupply_pos=[posy,posx]


    #----------------- build end


    else:
        print("Wrong input!")
