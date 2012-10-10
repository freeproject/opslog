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

之前采用facebook的开源方案fluent, 但是在实际的测试过程中，fluent仍然存在一些bug.比如日志正则格式不对，会造成cpu load飙升，信息不能入库。由于实在不怎么懂ruby, 所以采用类似的原理重新写了一个客户端。

#### server端: flask + mongodb
功能：mongodb作为数据存储层，flask作为前端展示层。

## _项目结构_

    client端：
    /admin/tailflog.py 

    server端：
    /data/project/opslog
    |-- documents.py
    |-- main.py
    |-- README.md
    |-- settings.py
    |-- static
    |   |-- bootstrap
    |   |   |-- css
    |   |   |   |-- bootstrap.css
    |   |   |   |-- bootstrap.min.css
    |   |   |   |-- bootstrap-responsive.css
    |   |   |   `-- bootstrap-responsive.min.css
    |   |   |-- img
    |   |   |   |-- glyphicons-halflings.png
    |   |   |   `-- glyphicons-halflings-white.png
    |   |   `-- js
    |   |       |-- bootstrap.js
    |   |       `-- bootstrap.min.js
    |   |-- bootstrap-daterangepicker
    |   |   |-- date.js
    |   |   |-- daterangepicker.css
    |   |   |-- daterangepicker.js
    |   |   `-- README.md
    |   |-- calendar.css
    |   |-- cal.js
    |   |-- datepicker
    |   |   |-- css
    |   |   |   `-- datepicker.css
    |   |   |-- js
    |   |   |   `-- bootstrap-datepicker.js
    |   |   `-- less
    |   |       `-- datepicker.less
    |   |-- daterangepicker
    |   |   |-- css
    |   |   |   `-- daterangepicker.css
    |   |   |-- js
    |   |   |   |-- date.js
    |   |   |   `-- daterangepicker.js
    |   |   `-- less
    |   |       `-- README.md
    |   |-- favicon.ico
    |   `-- highlight.js
    |-- templates
    |   |-- base.html
    |   |-- log
    |   |   |-- list_all.html
    |   |   |-- list_filter.html
    |   |   `-- list.html
    |   `-- srv
    |       |-- srv_info.html
    |       `-- title.html
    |-- TODO.md
    `-- tools
        |-- flask.sh
        |-- init_db.py
        |-- tailflog.py
        `-- uwsgi.sh

## _基本约定_

## _信息反馈_
