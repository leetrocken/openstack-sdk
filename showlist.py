import pymysql
pymysql_config = {
    'host': '172.16.180.10',
    'user': 'root',
    'password': '000000',
    # 'database': 'liluo',
    'charset': 'utf8'
}
conn = pymysql.connect(**pymysql_config)
cur = conn.cursor()
cur.execute('show databases')
res = cur.fetchall()
print(res)