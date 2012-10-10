## _项目介绍_

## _项目架构_

    +----------+
    | client 1 |              +--------+-------+
    | client 2 | -------------+------> |mongodb|
    | client 3 | ------------ | server |       |         +------+
    | client n |              |        | flask | ------> | user |
    | ......   |              +--------+-------+         +------+
    +----------+

#### client端: tailflog.py
功能：通过类似unix命令tail -f的方式，将信息转储到mongodb数据库。
之前采用facebook的开源方案fluent, 但是在实际的测试过程中，fluent仍然存在一些bug.
比如日志正则格式不对，会造成cpu load飙升，信息不能入库。由于实在不怎么懂ruby, 所
以采用类似的原理重新写了一个客户端。

#### server端: flask + mongodb
功能：mongodb作为数据存储层，flask作为前端展示层。

## _项目结构_

    client端：
    /opt/admin/tailflog.py  # tailflog.py程序 

    server端：
    /usr/local/nginx        # nginx安装目录
    /usr/local/mongodb      # mongodb安装目录
    /data/mongodb/          # mongodb数据目录
    /data/project/opslog    # flask程序目录
    
## _基本约定_

## _信息反馈_
