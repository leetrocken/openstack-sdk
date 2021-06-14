#!/usr/bin/python3

# -*- coding: UTF-8 -*-


import paramiko


def sshclient_execmd(hostname, port, username, password, *execmd):

#paramiko.util.log_to_file("paramiko.log") #日志路径

    for execmd_cmd in execmd:
        s = paramiko.SSHClient() # 绑定实例

        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())# 允许连接不在know_hosts文件中的主机

        s.connect(hostname=hostname, port=port, username=username, password=password) # 连接远程主机

        stdin, stdout, stderr = s.exec_command (execmd_cmd)#执行需要执行的Linux命令
        stdin.write("Y")

        b = (stdout.read())
        string=b.decode('utf-8','ignore') #将bytes 转为 字符串
        print(string)

    s.close() #退出连接

    return



hostname = '172.16.181.94'

port = 22

username = 'root'

password = '000000'

execmd1 = "mkdir -p /opt/123456"

execmd2 = "touch /opt/123456/test.txt"

execmd3 = "ls -l /opt/123456/test.txt"

execmd4 = "fdisk -l"

execmd5 = "df -h"

sshclient_execmd(hostname, port, username, password, execmd1,execmd2,execmd3,execmd4,execmd5)
