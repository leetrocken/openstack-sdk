# -*- coding: utf-8 -*-import os
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException# 导入对应产品模块的 client models。from tencentcloud.cvm.v20170312 import cvm_client, models
# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey, 此处还需注意密钥对的保密
    cred = credential.Credential("AKIDRm3BbsgxJVZVba7rGtNhspIc0NbgcWs3", "BD6pXTGvhVpM1gpq8VPAlGo1DRUj6JQv")

    # 实例化一个 http 选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "GET"  # get 请求 (默认为 post 请求)
    httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒 (默认60秒)
    httpProfile.endpoint = "cvm.ap-beijing.tencentcloudapi.com"  # 指定接入地域域名 (默认就近接入)

    # 实例化一个 client 选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA1"  # 指定签名算法
    clientProfile.language = "base64"  # 指定展示英文（默认为中文）
    clientProfile.httpProfile = httpProfile

    # 实例化要请求产品 (以 cvm 为例) 的 client 对象，clientProfile 是可选的。
    client = cvm_client.CvmClient(cred, "ap-beijing", clientProfile)

    # 实例化一个 cvm 实例信息查询请求对象,每个接口都会对应一个 request 对象。
    req = models.DescribeInstancesRequest()

    # 填充请求参数,这里 request 对象的成员变量即对应接口的入参。
    # 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义。
    respFilter = models.Filter()  # 创建 Filter 对象, 以 zone 的维度来查询 cvm 实例。
    respFilter.Name = "zone"
    respFilter.Values = ["ap-shanghai-1", "ap-shanghai-2"]
    req.Filters = [respFilter]  # Filters 是成员为 Filter 对象的列表

    # 这里还支持以标准 json 格式的 string 来赋值请求参数的方式。下面的代码跟上面的参数赋值是等效的。
    params = '''{
        "Filters": [
            {
                "Name": "zone",
                "Values": ["ap-shanghai-1", "ap-shanghai-2"]
            }
        ]
    }'''
    req.from_json_string(params)

    # 通过 client 对象调用 DescribeInstances 方法发起请求。注意请求方法名与请求对象是对应的。
    # 返回的 resp 是一个 DescribeInstancesResponse 类的实例，与请求对象对应。
    resp = client.DescribeInstances(req)

    # 输出 json 格式的字符串回包
    print(resp.to_json_string(indent=2))

    # 也可以取出单个值。
    # 您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义。
    print(resp.TotalCount)
except TencentCloudSDKException as err:
    print(err)