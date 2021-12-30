s = set("Hello") #set 自動分解字串
print(s)
################################
dic = {"apple":"蘋果","banana":"香蕉"}
dic["pig"] = "小豬" #添加新物品到原本字典

del dic["apple"]
print(dic)

print("apple" in dic)#判斷key 不會判斷value
print("蘋果" in dic)