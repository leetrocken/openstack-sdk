import requests
import json

os_auth_url = "http://172.16.180.10"
body = {"auth": {
    "identity": {
        "methods": ["password"], "password": {
            "user": {
                "id": "d7d5d39a4e1c4578b3dafcb2cba59e02",
                "password": "19880228"
            }
        }
    },
    "scope": {
        "project": {
            "id": "cf22d852f3e3480896f76f6334a72e90"
        }
    }
}
}
headers = {}
headers["Content-Type"] = "application/json"
headers["Accept"] = "*/*"


def get_token():
    os_auth_url_token = os_auth_url + ':35357/v3/auth/tokens'
    result = requests.post(os_auth_url_token, headers=headers, data=json.dumps(body)).headers["X-Subject-Token"]
    return result


def user_list():
    os_auth_url_user = os_auth_url + ':35357/v3/users'
    headers["X-Auth-Token"] = get_token()
    result = requests.get(os_auth_url_user, headers=headers).json()
    print(result)


user_list()
