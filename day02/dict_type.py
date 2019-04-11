import json
# 声明一个全量dict变量(字典)
adict={"name":"szc","pwd":"986524"}
# 这是一个字符串,不过他是一个json格式,也是字典格式
adictstr='{"name":"szc","pwd":"986524","1":"数字1"}'
if __name__ == '__main__':
    # print(adict['pwd'])
    # adict.pop('pwd')
    # print(adict)
    # str转dict格式
    print(type(adictstr))
    dict_str=json.loads(adictstr)
    print(type(dict_str))
    # 提取dict中的值
    print(dict_str['name'])
    # dict转str格式
    print(type(adict))
    dict_str=json.dumps(adictstr)
    print(type(adictstr))
    # 数字1乱码显示,不易阅读
    s = json.dumps(adictstr)
    print(s)
    # ensure_ascii=False 将中文转义.
    s = json.dumps(adictstr, ensure_ascii=False)
    print(s)
