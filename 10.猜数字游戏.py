import random
secret = random.randint(1,10) 
guess = 0
tries = 0  
print ("请你猜一猜从1到10，会是什么数字？")
print("你只有3次机会哦！")
while tries <3:  # 提供3次猜字机会
    guess = eval(input("请输入你猜的数字："))
    tries = tries +1
    if guess < secret:
        print ("太小了！！！！！！！！！！")
        continue
    elif guess > secret:
        print ("太大了！！！！！！！！！！")
        continue
    else:
        print("恭喜你，猜对了！")
        break
    
if guess != secret:
    print("很可惜，你猜错了！")
print("正确的数字为：" + str(secret))