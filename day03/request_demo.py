# 导入 requests 第三方包
import requests
def req_demo():

    # # 封装请求参数
    # data={"username": "admin", "password": "123456"}
    # # 发送请求 带上两个参数 url 和请求正文 json
    # response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    # # 获取字符串类型的响应报文
    # text_body = response.text
    # print(type(text_body))
    # print(text_body)
    # # 获取响应报文,并把报文转换成字典类型;报文必须是json类型才能转换
    # json_body=response.json()
    # print(type(json_body))
    # print(json_body)
    # # 断言响应状态码是否是200
    # assert 200==response.status_code
    # # 断言响应正文massage的值是否包含 成功 俩个字
    # assert '成功' in json_body['message']
    # # 断言响应正文code的值是否是200,注意响应正文的code值是int类型,所以不用in直接中==
    # assert 200 == json_body['code']
    # # 提取响应中的data的值(这是字典类型的值)
    # data_dict=json_body['data']
    # # 提取data_dict字典中 tokenHead的值
    # head_ = data_dict['tokenHead']
    # # 提取data_dict字典中 token的值
    # token_ = data_dict['token']
    # # 封装 请求头
    # d = {'Authorization': head_ + ' ' + token_}
    # # 发起 info 请求,传入指定参数tokenHead值为head
    # post_info = requests.get(url='http://192.168.60.132:8080/admin/info',headers=d)
    # # 打印响应正文
    # print(post_info.text)
    # assert 200 == json_body['code']
    # # get请求直接将参数放入url
    # requests_get = requests.get('http://192.168.60.132:8080/order/list?pageNum=1&pageSize=7', headers=d)
    # print(requests_get.text)
    # # 获取字典格式的响应正文
    # json = requests_get.json()
    # # 获取响应正文中的data的值
    # json_data_ = json['data']
    # # 获取json_data_字典的key为list的值,注意这个值是一个list的对象可以被遍历
    # list_ = json_data_['list']
    # # 遍历list_
    # for i in list_:
    #     print(i)
    pass
def shanchu_demo():
    data = {"username": "admin", "password": "123456"}
    response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    response1 = requests.post(url='http://192.168.60.132:8080/order/delete', json=data)
    json_body = response.json()
    print(json_body)
    assert 200 == response.status_code
def chaxun_demo():
    data = {"username": "admin", "password": "123456"}
    response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    response1 = requests.post(url='http://192.168.60.132:8080/order/list', json=data)
    json_body = response.json()
    print(json_body)
    assert 200 == response.status_code





if __name__ == '__main__':
    # req_demo()
    shanchu_demo()
    chaxun_demo()


    login_data = {"username": "admin", "password": "123456"}
    login_resp = requests.post(url='http://192.168.60.132:8080/admin/login', json=login_data)
    login_json = login_resp.json()
    print(login_json)

    # 提取响应中的data 的值(这是一个字典类型的值)
    data_dict = login_json['data']
    # 提取 data_dict 字典 中 tokenHead 的值
    token_head = data_dict['tokenHead']
    # 提取 data_dict 字典 中 token 的值
    token_ = data_dict['token']
    # 封装 请求头
    head = {'Authorization': token_head + ' ' + token_}

    # 发起 Info 请求 , 传入指定参数 headers 值为 head
    info_resp = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    info_json = info_resp.json()
    print(info_json)

    # 获取订单列表
    response = requests.get('http://192.168.60.132:8080/order/list?pageNum=1&pageSize=10&status=1&orderType=',
                            headers=head)
    print(response.text)
    response_json = response.json()
    json_data_ = response_json['data']
    list_ = json_data_['list']
    list__1 = list_[0]
    order_id = list__1['id']

    # 发货
    fahuo_data = [
        {
            "deliveryCompany": "顺丰",
            "deliverySn": "22222",
            "orderId": order_id
        }
    ]
    requests_post = requests.post('http://192.168.60.132:8080/order/update/delivery', headers=head, json=fahuo_data)
    print(requests_post.text)
    json = requests_post.json()

    # 关闭订单
    close_param = {'ids': order_id, 'note': 'guggg'}
    get = requests.post('http://192.168.60.132:8080/order/update/close', params=close_param, headers=head)
    print(get.text)
    json1 = get.json()
