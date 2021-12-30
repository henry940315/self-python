#file = open("data.text",mode="w")


# 語法
#open(檔案名稱,mode=模式)
#"w"寫  "r"讀  "r+"讀寫模式

#file.write #寫入檔案內容
#file.close()
print("-----------")

with open("data.txt",mode="w") as file:#第二種方法
    file.write("5")
    file.close