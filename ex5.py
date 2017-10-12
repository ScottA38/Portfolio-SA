#set variable bottles to 100
bottles= 100

#create condition
while (bottles > 0):
    bottles -= 1
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} of beer.")
        print(f"Take one down, pass it around, {bottles} bottles of beer on the wall...")
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall, of beer!")
        print("So take it down, pass it around, no more bottles of beer on the wall!")


#tutor example

#for p in range(99, 0 , -1):
#    print(f"{p} bottles of beer on the wall, {p} bottles of beer.")
#    print(f"Take one down, pass it around, {p} of beer on the wall..")
#print("Take one down, pass it around, no more bottles of beer on the wall!")
