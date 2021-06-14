# _*_ coding:UTF-8 _*_
from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client
def get_keystone_session():
    auth = v3.Password(auth_url="http://10.144.196.177:5000/v3",username="admin",password="Ywx@123..",project_domain_name="demo",project_name="admin",user_domain_name="demo")
    sess = session.Session(auth=auth)
    return sess
def get_nova_client():
    sess = get_keystone_session()
    nova = client.Client(2,session=sess)
    return nova
if __name__ == "__main__":
    create=get_nova_client()
    list = create.flavors.list()
    for ls in list:
        if(ls.name == "test"):
            create.flavors.delete(ls.id)
    create.flavors.create(name="lsc",vcpus="1",ram="1024",disk="20",flavorid="199999")
    print("云主机类型创建成功")

