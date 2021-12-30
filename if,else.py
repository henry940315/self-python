s1 = int(input("Enter a word 1    ") )
s2 = int(input("Enter a word 2    ") )
s3 = input("+ - * /     " )
if(s3 == "+"):
    print(s1 + s2)
elif(s3 == "-"):
    print(s1 - s2)
elif(s3 == "*"):
    print(s1 * s2)
elif(s3 == "/"):
    print(s1/s2)
else:
    print("you enter a wrong symbol")
