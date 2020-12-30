#autobuilder by czkawuszka uwuowo
import numpy as np
print("Hello to etch-a-sketch!")
print(" ")
print("Creating table...")
print(" ")


len=50
hash_materials=0

cord = [['-' for x in range(len)] for y in range(20)]

print("Table finished!")


posy, posx = 0, 0
cord[posy][posx]='o'
painting='n'
erasing='n'
temp2='-'

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

help()
while True:
    y=0
    x=0
    while(y<20):
        while(x<len):
            print(cord[y][x], end='')
            x+=1
        x=0
        y+=1
        print(" ")

    p_input=str(input('Command: '))
    if(p_input=='up' or p_input=='u'):
        if(posy==0):
            print("You're already at the top end of the space")
        else:
            posy-=1
            temp=cord[posy][posx]
            cord[posy][posx]='o'
            cord[posy+1][posx]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
                hash_materials+=1
            elif(temp=='#' and erasing=='y'):
                temp2='-'
                hash_materials-=1
            else:
                temp2=temp
    elif(p_input=='down' or p_input=='d'):
        if(posy==19):
            print("You're already at the bottom end of the space")
        else:
            posy+=1
            temp=cord[posy][posx]
            cord[posy][posx]='o'
            cord[posy-1][posx]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
                hash_materials+=1
            elif(temp=='#' and erasing=='y'):
                temp2='-'
                hash_materials-=1
            else:
                temp2=temp
    elif(p_input=='left' or p_input=='l'):
        if(posx==0):
            print("You're already at the left end of the space")
        else:
            posx-=1
            temp=cord[posy][posx]
            cord[posy][posx]='o'
            cord[posy][posx+1]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
                hash_materials+=1
            elif(temp=='#' and erasing=='y'):
                temp2='-'
                hash_materials-=1
            else:
                temp2=temp
    elif(p_input=='right' or p_input=='r'):
        if(posx==49):
            print("You're already at the right end of the space")
        else:
            posx+=1
            temp=cord[posy][posx]
            cord[posy][posx]='o'
            cord[posy][posx-1]=temp2
            if(temp=='-' and painting=='y'):
                temp2='#'
                hash_materials+=1
            elif(temp=='#' and erasing=='y'):
                temp2='-'
                hash_materials-=1
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
    elif(p_input=='help')
        help()
    elif(p_input=='build'):
        print("///////////////////////////////")
        print("You chose: build")
        print("Warning! This action cant be undone!")
        print("Confirm? y/n...")
        while True:
            build_input=str(input())
            if(build_input=='y'):
                print("Starting build!")
                while True:
                    print("Materials needed: #: "+ str(hash_materials))
                    break
            elif(build_input=='n'):
                print("Why did you type build then?")
                break
            else:
                print("Wrong input! Try again.")
            break

        print("///////////////////////////////")
    else:
        print("Wrong input!")
