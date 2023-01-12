from playsound import playsound
from time import sleep

print("do you want to lisen to music")

x = input("enter y/n :") 
if (x== "y"): 
    z = input(" choese 1/2 : ")

if( z == "1"):
    print(1)
    sleep(1)
    print(2)
    sleep(1)
    print(3)
    sleep(1)
    while True:
        playsound("sounds//ice cream.mp3")

if( z == "2"):
    print(1)
    sleep(1)
    print(2)
    sleep(1)
    print(3)
    sleep(1)
    while True:
        playsound("sounds//kemetsu no yaba.mp3")