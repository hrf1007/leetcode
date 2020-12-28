s = 'DerisWeng'
# 占位符{}，默认顺序
print ('{} {}'.format('one', 'two'))
print('我的姓名为{},年龄{}岁,爱好{}'.format('DerisWeng','18','dancing'))  
# 占位符{}，指定顺序
print ('{1} {0}'.format('one', 'two'))
print('我的姓名为{0},年龄{1}岁,爱好{2}'.format('DerisWeng','18','dancing'))  
# 默认左对齐，占30个字符
print ('{:30}'.format(s)) 
# 默认左对齐，占30个字符，此处逗号表示两个字符串按顺序显示
print ('{:30}'.format(s),'abc')  
# 右对齐，占30个字符
print ('{:>30}'.format(s) ) 
# 填充字符为-，^表示以居中方式显示，所有字符占30个位置
print ('{:-^30}'.format(s) ) 
# 填充字符为-，>表示以靠右方式显示，所有字符占20个位置
# 填充符号可以是符号、数字和字母
print ('{:->20}'.format(s) ) 
# 填充字符为+，<表示以靠左方式显示，所有字符占20个位置
print ('{:+<20}'.format(s)) 
# 填充字符为q，<表示以靠左方式显示，所有字符占20个位置
print ('{:q<20}'.format(s))  
# 填充字符为1，<表示以靠左方式显示，所有字符占20个位置
print ('{:1<20}'.format(s))  
# 填充字符为*，>表示以靠右方式显示，所有字符占20个位置
print ('{:*>20}'.format(s))  
# 保留小数点后两位
print ('{:.2f}'.format(12345678))  
# 千分位分隔
print ('{:,}'.format(12345678)) 
# 0表示format中的索引号index
print ('{0:b},{0:c},{0:d},{0:o},{0:x}'.format(42)) 
# 0对应42，1对应50
print ('{0:b},{1:c},{0:d},{1:o},{0:x}'.format(42,50))  
# 默认index为0 
print ('{:b}'.format(42)) 
# 字符串s的最大输出长度为2
print ('{:.2}'.format(s))  
# 中文
print("{:好<20}".format(s))