# 用sub()函数删除注释
import re
phone="0577-8668-1001"
num=re.sub(r'#.*$',"",phone)
print("电话号码:",num)
num1=re.sub(r'\D',"",num)
print("电话号码:",num1)