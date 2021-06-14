# _*_ coding:UTF-8 _*_
from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client
def get_session():
    auth = v3.Password(auth_url="http://:5000/v3",username="admin",password="000000",domain_name="demo",project_name="admin",project_domain_name="admin",user_domain_name="admin")
    sess = session.Session(auth=auth)
    return sess
def get_nova_client():
    sess = get_session()
    nova = client.Client(2,session=sess)
    return nova
if __name__ == "__main__":
    flavor_create = get_nova_client()
    list = flavor_create.flavors.list()
    for show in list:
        if(show.name == "test"):
            flavor_create.flavors.delete(show.id)
    flavor_create.flavors.create(name="test",vcpus="1",ram="1024",disk="20",flavorid="199999")
    print("云主机类型创建成功")