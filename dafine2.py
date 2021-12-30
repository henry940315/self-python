#建立一個開方的函數

def power(base,exp):
    return base**exp

value = power(3,4)
print(value)

print("------------------")
#建立一個除式的函數
def devide(n,b):
    return n/b
value1 = devide(4,2)
print(value1)

print("------------------------")
#無限參數
def arg(*ns):
    sum = 0
    for x in ns:
        sum = sum + x
    print(sum / len(ns))
        
arg(5,4)
arg(5,7,8)
arg(5,1,2,7)