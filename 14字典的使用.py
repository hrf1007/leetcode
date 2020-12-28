dcountry={"中国":"北京","美国":"华盛顿","法国":"巴黎"}
dcountry.keys()
list(dcountry.values())
dcountry.items()
'中国' in dcountry
dcountry.get('美国','悉尼')
dcountry.get('澳大利亚','悉尼')
for key in dcountry:
    print(key)
    