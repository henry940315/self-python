#定義函式
#函式內部程式碼 若沒有呼叫函數 就不會執行

def multiply(a1,a2):
    return a1 * a2
   
#呼叫函式
value = multiply(4,5)
print(value)

revalue = multiply(5,7) + multiply(8,9)
print(revalue)

print("------------------------")
def caculate(s1,s2):
   
    sum = 0
    for n in range(s1,s2+1):
        sum=sum + n
    print(sum)
    
var = caculate(1,10)
print(var)