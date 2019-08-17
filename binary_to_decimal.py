'''
Write a program that prompts the user for a binary number with the length from 1 to 20 digits then output its corresponding decimal value. Your program will output Error if the length of the binary number is not valid.
'''
# Request input from the user
usrInput = input("Enter your binary number:")
# Implement your logic here
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