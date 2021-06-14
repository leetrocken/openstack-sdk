import requests
import json
from oslo_utils import strutils
from oslo_utils import uuidutils

os_auth_url = "http://172.16.200.32"
body = {"auth": {
    "identity": {
        "methods": ["password"], "password": {
            "user": {
                "id": "d3d87846736d47018d4fa1d569e246c5",
                "password": "000000"
            }
        }
    },
    "scope": {
        "project": {
            "id": "b4b7488a69f548518523041f1d50be4c"
        }
    }
}
}
headers = {}
headers["Content-Type"] = "application/json"
headers["Accept"] = "*/*"
def get_token():
    get_token_url=os_auth_url+':35357/v3/auth/tokens'
    result=requests.post(get_token_url,headers=headers,data=json.dumps(body)).headers['X-Subject-Token']
    return result

def user_list():
    user_list_url=os_auth_url+':35357/v3/users'
    headers['X-Auth-Token']=get_token()
    result=requests.get(user_list_url,headers=headers).json()
    print(result,'\n')

def images_list():
    images_list_url=os_auth_url+':9292/v2/images'
    headers['X-Auth-Token']=get_token()
    result=requests.get(images_list_url,headers=headers).json()
    print(result,'\n')
user_list()

# def volume_create():
#     volume_create_url = os_auth_url + ':8774/v2.1/flavors'
#     result = requests.get(volume_create_url,headers=headers).json()
#     print(result)

# try:
#     flavor_create = os_auth_url + ':8774/v2.1/flavors'
#     headers['X-Auth-Token']=get_token()
#     requests.post(flavor_create,headers=headers).json()
#     req=requests.ResizeDiskRequest()
#     params={
#     }
#     req.from_json_string(json.dumps(params))
#     resp=requests.ResizeDisk(req)
#     print(resp.to_json_string())
# def create(name, memory, vcpus, root_gb, ephemeral_gb=0, flavorid=None,
#            swap=0, rxtx_factor=1.0, is_public=True, description=None):
#     """Creates flavors."""
#     if not flavorid:
#         flavorid = uuidutils.generate_uuid()
#
#     kwargs = {
#         'memory_mb': memory,
#         'vcpus': vcpus,
#         'root_gb': root_gb,
#         'ephemeral_gb': ephemeral_gb,
#         'swap': swap,
#         'rxtx_factor': rxtx_factor,
#         'description': description
#     }
#
#     if isinstance(name, str):
#         name = name.strip()
#
#     # NOTE(vish): Internally, flavorid is stored as a string but it comes
#     #             in through json as an integer, so we convert it here.
#     flavorid = str(flavorid)
#
#     # NOTE(wangbo): validate attributes of the creating flavor.
#     # ram and vcpus should be positive ( > 0) integers.
#     # disk, ephemeral and swap should be non-negative ( >= 0) integers.
#     flavor_attributes = {
#         'memory_mb': ('ram', 1),
#         'vcpus': ('vcpus', 1),
#         'root_gb': ('disk', 0),
#         'ephemeral_gb': ('ephemeral', 0),
#         'swap': ('swap', 0)
#     }
#
#     for key, value in flavor_attributes.items():
#         headers['X-Auth-Token']=get_token()
#
#     # rxtx_factor should be a positive float
#     try:
#         kwargs['rxtx_factor'] = float(kwargs['rxtx_factor'])
#         if (kwargs['rxtx_factor'] <= 0 or
#                 kwargs['rxtx_factor'] > db.SQL_SP_FLOAT_MAX):
#             raise ValueError()
#     except ValueError:
#         msg = (_("'rxtx_factor' argument must be a float between 0 and %g") %
#                db.SQL_SP_FLOAT_MAX)
#         raise exception.InvalidInput(reason=msg)
#
#     kwargs['name'] = name
#     kwargs['flavorid'] = flavorid
#     # ensure is_public attribute is boolean
#     try:
#         kwargs['is_public'] = strutils.bool_from_string(
#             is_public, strict=True)
#     except ValueError:
#         raise exception.InvalidInput(reason=_("is_public must be a boolean"))
#
#     flavor = objects.Flavor(context=context.get_admin_context(), **kwargs)
#     flavor.create()
#     return flavor