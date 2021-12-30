#一行一行的讀取 
sum = 0
with open("readme.txt",mode="r") as file:
    for line in file:
        sum =sum + int(line) 
        sum = sum+1+int(line) 
print(sum)