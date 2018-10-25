---
layout: post
title: "Ubuntu 18.04简单部署ShareLaTeX"
date: 2018-10-25
description: ""
tag: LaTeX
---

# 参考
- [ArchLinux 部署ShareLaTex并且配置中文支持](https://blog.csdn.net/hello_percy/article/details/72147414)
- [Quick Start Guide](https://github.com/sharelatex/sharelatex/wiki/Quick-Start-Guide)
-[本地部署 ShareLatex](https://haoyu.love/blog640.html)
-[Get Docker CE for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

# 依赖安装
## Docker-ce and Docker-compose
参见[Docker-ce](https://docs.docker.com/install/linux/docker-ce/ubuntu/)与[Docker-compose](https://docs.docker.com/compose/install/)。

## Redis and Mongodb
```Shell
$ sudo apt install redis-server
$ sudo apt install mongodb
```

# 安装ShareLaTeX
## sharelatex
使用*Docker*安装*sharelatex*，*tex*编译环境默认为2017版本，后续将介绍如何更新。
```Shell
$ docker pull sharelatex/sharelatex
```

## Using a compose file
```Shell
$ curl -O https://github.com/sharelatex/sharelatex/raw/master/docker-compose.yml
```
此时需要修改*docker-compose.yml*文件，[配置文件](https://github.com/sharelatex/sharelatex/wiki/Configuring-ShareLaTeX)信息。如果80端口已经被占用，需要修改如下选项，其中*XX*为使用的端口
```
services:
    sharelatex:
        ports:
            - XX:80
```
进行下一步，部署*sharelatex*，并且添加管理员用户，邮箱需要自己修改，输入后会有链接显示在命令行，需要打开修改账户密码。
```Shell
$ sudo docker-compose up

$ docker exec sharelatex /bin/bash -c "cd /var/www/sharelatex; grunt user:create-admin --email joe@example.com"
```
如此，就可以在特定的端口访问到*sharelatex*主页了。

# 登陆container的shell
```Shell
$ docker ps
CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS              PORTS                  NAMES
056c250ddb2a        sharelatex/sharelatex   "/sbin/my_init"          15 hours ago        Up 15 hours         0.0.0.0:1024->80/tcp   sharelatex
8234a9e397e1        mongo                   "docker-entrypoint.s…"   17 hours ago        Up 15 hours         27017/tcp              mongo
79eb20131893        redis                   "docker-entrypoint.s…"   17 hours ago        Up 15 hours         6379/tcp               redis
```
*sharelatex*的container ID是*056c250ddb2a*，再执行
```Shell
$ docker inspect -f {{.State.Pid}} 056c250ddb2a
14510
```
看到PID是14510，最后使用root登陆到*sharelatex*的shell了。
```Shell
$ sudo nsenter --target 14510 --mount --uts --ipc --net --pid
root@056c250ddb2a:/#
```

# TeXLive Update
升级*TeXLive*
```Shell
docker exec sharelatex tlmgr install scheme-full
```
使用*tlmgr*升级*TeXLive*会有以下报错
```Shell
tlmgr: Remote repository is newer than local (2017 < 2018)
Cross release updates are only supported with
  update-tlmgr-latest(.sh/.exe) --update
Please see https://tug.org/texlive/upgrade.html for details.
```
根据提示去寻找*update-tlmgr-latest.sh*进行配置。
```Shell
root@056c250ddb2a:/# wget http://mirror.ctan.org/systems/texlive/tlnet/update-tlmgr-latest.sh
root@056c250ddb2a:/# sh update-tlmgr-latest.sh
```
最后更新*tlmgr*，接下来的任务就是等待了。
```Shell
root@056c250ddb2a:/# tlmgr option repository http://mirrors.ustc.edu.cn/CTAN/systems/texlive/tlnet
root@056c250ddb2a:/# tlmgr install scheme-full
```

# 配置中文字体
参考[ArchLinux 部署ShareLaTex并且配置中文支持](https://blog.csdn.net/hello_percy/article/details/72147414)，方法适用。
![](/images/posts/2018-10-25-sharelatex-1.jpg)

# 成果
![](/images/posts/2018-10-25-sharelatex-2.jpg)


---

Iydon
