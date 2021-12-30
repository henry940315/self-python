#import sys
import sys
sys.path.append("module")#在模組列表新增搜尋路徑
print(sys.path)

print("-----------------------")
import module.geomatry
#使用模組功能
result = module.geomatry.distance(0,0,10,20)
print(result)







