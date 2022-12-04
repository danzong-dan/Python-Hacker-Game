import time


def p(txt):
    for i in txt:
        print(i, end="")
        time.sleep(0.1)
    print(" ")


def inp():
    return input("@<[PHG] "+str("C:/")+"/"+str("new_user")+"/"+str("computer")+">>>")


p("welcome to PHG WiKi")
p("这里有你需要的指令帮助")
p("输入您的选项")
p('''
1.初级指令与入门教学
2.高级指令
3.Hacker应用栏
4.主机常识
5.Hacker Internet 安全协议
输入您的选择
''')
choose = input("")


def simple_Code():
    p("初级指令，指的是基础的电脑操作与文件处理，适合新手使用")
    p("是否开始教学?")
    f = input("Y/N :")
    if f == "Y":
        p("当你打开PHG的时候，会看到这样的一个命令行")
        inp()
        p("在这里输入你的代码与命令")
        p("我们讲解一些简单的代码吧~")
        p('''
                                不多不少的指令
        --------------------------------------------------
        1.tree 遍历目录
        2.mail 邮箱(查询下一个关卡)
        3.ipconfig 查询本电脑的IP
        4.delete [文件名] 删除文件
        5.install [文件名] 将install文件夹的【文件】 传入 本地
        6.scp [文件名]   复制一份文件(由远程计算机连接时使用)
        7.cd [目录] 切换目录
        8. mc 查询本电脑所有目录
        还有其他指令，请跳转至PHG wIkI 来查看
        ''')
        p("你可以打开PHG来尝试一下")
        p("入门教学就到这里了~")


simple_Code()
