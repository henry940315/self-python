s1 = {5,6,8,4,7}
print(5 in s1)#判斷5有沒有在s1 
print(10 not in s1)

#########
s2 = {7,9,6,5}
s3 = {8,5,4,1}
s4 = s1&s2&s3#交集 取相同的資料
s5 = s1|s2|s3#聯集 取所有不同的資料
s6 = s1 - s2
s7 = s1^s2
print(s4)
print(s5)
print(s6)
print(s7)