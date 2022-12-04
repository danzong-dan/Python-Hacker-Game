import ctypes
import re
import sys
import time

# 可以增加一个管理员权限
# 来操控一些文件
fffff = ['passguesser.exe', 'sniffer.exe']


class Computer(object):
    def __init__(self, ip, username, cpname, pd, port):
        self.ip = ip
        self.username = username
        self.cpname = cpname
        self.pd = pd
        self.port = port
        self.data_file = []
        self.install_file = []
        self.story = 0
        self.dir = "C:/"
        self.connect = []


cp1 = Computer("178.121.90.10", "root", "hh", "123456", "256")
google = Computer("26.100.10.91", "google_the_best", "hh", "123456", "243")
# 定义一台远程主机的内置文件
# 说实话，这几行代码完全可以改进 —— JC
# cp1类
cp1.data_file.append("wget.exe")
cp1.data_file.append("log.txt")
cp1.data_file.append("passguesser.exe")
cp1.data_file.append("tracer.exe")
# google 类
google.data_file.append("log.connection")
google.data_file.append("main.php")
google.data_file.append("meeting.html")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def p(txt):
    for i in txt:
        print(i, end="")
        time.sleep(0.1)
    print("")


def inp(Computer):
    return input("@<[PHG] "+str(Computer.dir)+"/"+str(Computer.username)+"/"+str(Computer.cpname)+">>>")


def main():
    global username, pd, cpname, data_file, install_file
    print('''
    version DEMO
        本次版本为测试
    ##################  #               #    ##################
    #                #   #               #    #
    #                #   #               #    #
    #################   #               #    #
    #                   #               #    #
    #                   #################    #
    #                   #               #    #           ###########
    #                   #               #    #                 #
    #                   #               #    #                 #
    #                   #               #    ###################
    ''')
    p("欢迎来到【PHG】,社区PYTHON圈里的黑客游戏")
    p("输入您的选择")
    p("1.开始你的黑客之路(为啥一个选项也要输入？？？)")
    flaf = input(">>")
    if flaf == "1" or flaf == 1:
        username = input("输入您的名字")
        pd = input("输入主机密码")
        cpname = input("输入主机名")


f = main()
cp = Computer("179.121.89.10", username, cpname, pd, "92")


def telnet(Computer,):
    p("正在连接远程主机"+Computer.ip+":"+Computer.port)
    p("输入主机用户名login:")
    un = input("")
    p("输入主机密码password:")
    pdd = input("")
    if un == Computer.username and pdd == Computer.pd:
        p("连接成功!")
        Computer.connect.append(cp.ip)
    if Computer.username == google.username:
        while True:
            if main_loop(google):
                break
        return True
    elif Computer.username == cp1.username:
        while True:
            if main_loop(cp1):
                break
        return True
    else:
        p("密码错误 或是 IP错误  连接失败")
        return False


def install(f, Computer):
    for i in f:
        if i in Computer.install_file:
            Computer.data_file.append(i)
            p("ok")


def dc(Computer):
    p("已经断开了连接")


def mail(file):
    p("------欢迎来到【邮箱】----------")
    with open(file, "r", encoding="UTF-8")as f:
        print(f.read())
    return True


def scp(Computer, f):
    p(f)
    for i in f:
        if i in cp1.data_file:
            Computer.install_file.append(i)
            p("ok")


def wget(Computer, f):
    nf = Computer.install_file
    for i in f:
        if i in fffff:
            nf.append(i)
            p("ok")


def passguesser(Computer):
    p("用户名login："+str(Computer.username))
    p("密码password:"+str(Computer.pd))
    return Computer.username, Computer.pd


def tracer(Computer):
    p("此电脑的端口为"+Computer.port)
    p("最近连接的远程计算机")
    return Computer.port


def log_personal_hackers(Computer):
    p("|——"+str(Computer.username))
    p("    |——"+str(Computer.cpname))
    for i in Computer.data_file:
        p("|——"+str(i))
    for i in Computer.install_file:
        p("|——"+str(i))
    p("port:"+str(Computer.port))
    p("ip:"+str(Computer.ip))


def tree(Computer):
    # 此功能为梳理目标计算机的文件
    print("—————————————————————————")
    p("|——"+str(Computer.dir)+":")
    if Computer.dir == '/data':
        for i in Computer.data_file:
            p("/data |————"+str(i))
    if Computer.dir == '/Is':
        p("|——Is(Install文件夹):")
        for i in Computer.install_file:
            p("/Is |————"+str(i))
    if Computer.dir == 'C:/':
        for i in Computer.data_file:
            p("/data |————"+str(i))
        for i in Computer.install_file:
            p("/Is |————"+str(i))


def delete(Computer, m):
    p(str(m))
    for i in m:
        p("start loop!")
        if i in Computer.install_file:
            Computer.install_file.remove(str(i))
            p("ok")
        if i in Computer.data_file:
            Computer.data_file.remove(str(i))
            p("ok")


def readCon(Computer):
    return Computer.connect


def cG():
    p("[msg] 收到消息，请输入mail来查看邮箱")


def ftp(Computer):
    p("连接用户IP"+str(Computer.ip))


f = 1


def keepAdmin(Computer, b):
    if b:
        p("开启权限,可更改内容")
    return b


flag32 = False


def main_loop(Computer):
    global f, flag32
    fff = False

    m = inp(Computer)
    # print(Computer.file)
    # print(Computer.install_file)
    if Computer.story == 0:
        cG()
        Computer.story += 1
    if Computer.story == 1:
        for i in cp1.connect:
            if i == cp.ip:
                Computer.story += 1
                cG()
    if Computer.story == 2:
        for i in cp.data_file:
            if i == "wget.exe":
                Computer.story += 1
                cG()
    if Computer.story == 3:
        for i in cp.data_file:
            if i == "passguesser.exe":
                Computer.story += 1
                cG()
    if Computer.story == 4:
        if "main.php" not in google.data_file and "log.connection" not in google.data_file:
            Computer.story += 1
            cG()
    if Computer.story == 5:
        p("the end~")
    if m == "mail":
        mail("story"+str(Computer.story)+".txt")

    elif 'telnet' in m:
        
        flag = 1
        if flag == 1:
            ip = input("请再次输入远程电脑的IP或是 [ip](:port) 端口>>")
            if ip == cp1.ip or ip == cp1.ip + ":" + cp1.port:
                telnet(cp1)
            if ip == google.ip or ip == google.ip + ":" + google.port:
                telnet(google)
        else:
            p("没有此远程计算机")
    elif 'wgetine' in m:
        flag5 = 1
        if 'wget.exe' in Computer.data_file:
            if flag5 == 1:
                wget(Computer, m.split('wgetine '))
        else:
            p("wgetine 不是指令 或 程序")
    elif 'passguesser' == m:
        if m+".exe" in Computer.data_file:
            ip = input("输入电脑[IP]或 [ip](:端口)>>")
            if ip == cp1.ip or ip == cp1.ip + ":" + cp1.port:
                p(passguesser(cp1))
            elif ip == google.ip or ip == google.ip + ":" + google.port:
                p(passguesser(google))
        else:
            p('passguesser 不是指令 或 程序')
    elif 'tracer' == m:
        if m+".exe" in Computer.data_file:
            ip = input("输入电脑[IP]或 [ip](:端口)>>")
            if ip == cp1.ip or ip == cp1.ip + ":" + cp1.port:
                tracer(cp1)
        else:
            p('tracer 不是指令 或 程序')
    elif 'scp' in m:
        flag2 = 1
        if flag2 == 1:
            scp(cp, m.split('scp '))
    elif m == 'dc':
        dc(Computer)
        fff = True
    elif m == 'tree':
        tree(Computer)
    elif 'install' in m:
        flag3 = 1
        if flag3 == 1:
            install(m.split('install '), Computer)
    elif 'keepAdmin' in m:
        flag556 = 1
        if flag556 == 1:
            flag32 = keepAdmin(Computer, m.split('keepAdmin '))
    elif 'delete' in m:
        if Computer.username == "google_the_best":
            if flag32:
                delete(Computer, m.split('delete '))
            else:
                p("您未拥有管理员权限..")
        else:
            delete(Computer, m.split('delete '))
    elif m == 'help':
        print('''
                请跳转至PHG wIkI 来查看
        
        ''')

    elif 'detail' in m:
        mf2 = m.split('detail ')
        p("暂无相关内容")
    elif m == 'ipconfig':
        p("本电脑IP地址为："+str(Computer.ip))
    elif 'cd' in m:
        c = m.split('cd ')
        cf = 0
        print(c)
        for i in c:
            if i == '/data':
                Computer.dir = i
                cf += 1
            elif i == 'C:/':
                Computer.dir = i
                cf += 1
            elif i == '/Is':
                Computer.dir = i
                cf += 1
        if cf == 0:
            p("没有此文件目录,请重新键入...")
    elif m == "mc":
        log_personal_hackers(Computer)
    else:
        p(str(m)+"不是一个指令或文件,请重新键入!")
    return fff


if __name__ == '__main__':
    if is_admin():
        while True:
            main_loop(cp)
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, __file__, None, 1)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(
                sys.executable), unicode(__file__), None, 1)
