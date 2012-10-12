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
功能：mongodb采用固定集合作为数据存储层，每集合空间达到10G会自动回滚。
flask作为前端展示层，查询规则支持PCRE标准正则语法。

## _项目文件结构_

    client端：
    /opt/admin/tailflog.py  # tailflog.py程序 

    server端：
    /opt/nginx        # nginx安装目录
    /opt/mongodb      # mongodb安装目录
    /opt/mongodb/data         # mongodb数据目录
    /opt/project/opslog    # flask程序目录
    
## _基本约定_

## _信息反馈_
