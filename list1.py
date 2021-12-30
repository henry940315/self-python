grades = [99,58,74,59]
print(grades[0])
#把55更換到0位置
grades[0]=55
print(grades)
#連續刪除
grades[1:3]=[]
print(grades)
#插入字串
grades = grades + [12,89]
print(grades)
#列表長度
length = len(grades)
print(length)