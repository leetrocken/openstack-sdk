import json

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cbs.v20170312 import cbs_client,models
try:
    cred=credential.Credential("AKIDyjKfkNm8ZjeLlbvzGH7JaiaBZps09CZk","4vXq9u75t3zgqjqnV3Xt5QW5QVFpBNwGu")
    httpProfile = HttpProfile()
    httpProfile.endpoint="cbs.tencentcloudapi.com"
    clientProfile=ClientProfile()
    clientProfile.httpProfile=httpProfile
    client=cbs_client.CbsClient(cred,"ap-xxx",clientProfile)
    req=models.ResizeDiskRequest()
    params={
        "DiskId": "id",
        "DiskSize": 50
    }
    req.from_json_string(json.dumps(params))
    resp=client.ResizeDisk(req)
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)