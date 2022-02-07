import random

num = 3
while num <= 21:
    print(num)
    num += 3
    
choice = 1
print("enter a number or 0 to quit")
choice = int(input())
while( choice > 0):
    print("Snurfle")
    choice -= 1
    
def MonsterGen(biome):
    change = random.randrange(1, 1000)
    if biome == 'd':
        if num < 20:
            print ("Husk appeared")
        elif num < 50:
            print("Spider appeared")
        elif num < 100:
            print("Skeleton appeared")
    if biome == 'f':
        if num < 10:
            print ("Witch appeared")
        elif num < 40:
            print("Zombie appeared")
        elif num < 70:
            print("Skeleton appeared")
        elif num < 100:
            print("Nothing spawns")


mon = 'a'
while mon != 'q':
    print("Enter biome or q to quit")
    mon = input()
    if choice != 'q':
        MonsterGen(mon)
