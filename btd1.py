usrInput = input("Enter your binary number:")
t = usrInput[::-1]
length=len(usrInput)
total=0
exp=0
while length > 20:
    print("Error")
    quit()

while exp < length:
    if t[exp] =="1":
        total+=2**int(exp)
    exp+=1
print(total)
