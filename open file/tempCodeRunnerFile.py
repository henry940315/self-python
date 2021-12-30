file = open("data.text",mode="w",endcoding="utf-8")
# 語法
#open(檔案名稱,mode=模式)
#"w"寫  "r"讀  "r+"讀寫模式

file.write("雞雞")#寫入檔案內容
file.close()