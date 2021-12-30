n = 0
while n <= 5:
    if n ==3:
        break#離開迴圈
    print(n)
    n += 1
print("最後的n",n)

print("-------------------")

for x in [0,1,2,3]:
    if x%2 == 0:
        continue #忽略下方程式 直接跑下一圈
    print(x)
    
print("最後的x",x)
print("------------------")
sum =0
for i in range(11):
    sum =sum + i
else:
    print(sum)

print("----------------")
number = int(input("Enter a word") )

for c in range(number):
    if c*c == number:
        print("是平方數")
        break#強制停止迴圈 不會執行else
else:
    print("不是平方數")
    
