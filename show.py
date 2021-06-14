from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client
def get_keystone_session():
    auth = v3.Password(auth_url="http://172.16.180.10:5000/v3",username="admin",password="Ywx@123..",project_name="admin",user_domain_name="demo",project_domain_name="demo")
    sess = session.Session(auth=auth)
    return sess
def get_nova_client():
    sess=get_keystone_session()
    nova=client.Client(2,session=sess)
    return nova
if __name__ == "__main__":
    sl=get_nova_client()
    ss=sl.flavors.list()
    for i in ss:
        if(i.name == 'iaas'):
            print(i.id)

