import random as r

l = 0
v = 0
t = 0
up = 0
cp = 0
turns = 1
user = 0
a = ["rock","paper","scissor"]
while True:
    comp = r.randint(1,3)
    turns += 1
    print("Loses:",l)
    print("Ties:",t)
    print("Victories:",v)
    print("Computer has",cp,"points")
    print("User has",up,"points")
    print("rock -> 1")
    print("paper -> 2")
    print("scissor -> 3")
    print("enter the number for user")
    try:
        user = int(input())
        if user == 1 and comp == 3:
            print("user played",a[user-1])
            print("comp played",a[comp-1])
            v += 1
            up += 1
        elif user == 2 and comp == 1:
            print("user played",a[user-1])
            print("comp played",a[comp-1])
            v += 1
            up += 1
        elif user == 3 and comp == 2:
            print("user played",a[user-1])
            print("comp played",a[comp-1])
            v += 1
            up += 1
        elif user == comp:
            print("user played",a[user-1])
            print("comp played",a[comp-1])
            t += 1
            up += 1
            cp += 1
        else:
            print("user played",a[user-1])
            print("comp played",a[comp-1])
            l += 1
            cp += 1
    except Exception as e:
        print("please play within range!!!")