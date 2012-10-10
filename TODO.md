# 项目部署
可以根据需要选择自动或者手动
## 自动:
/opt/project/opslog/tools/setup.py
## 手动:
### mongodo环境部署
/opt/project/opslog/tools/init_db.py
### flask环境部署
/opt/project/opslog/tools/flask.sh
### nginx环境部署
    cat > /etc/nginx/nginx.conf << EOF
    worker_processes  1;
    events {
        worker_connections  1024;
    }
    http {
        include       mime.types;
        default_type  application/octet-stream;
        sendfile        on;
        keepalive_timeout  65;
        server {
            listen       80;
            server_name  0.0.0.0;
        root /data/project/opslog/static;
            location / { 
            include uwsgi_params; 
            uwsgi_pass unix:/tmp/uwsgi.sock; 
            }
        }
    }
    EOF

## 客户端部署
复制
/opt/project/opslog/tools/tailflog.py 
到客户机
/opt/admin/tailflog.py
运行实例
    python /admin/tailflog.py /var/log/auth.log opslog auth syslog
    参数：/var/log/auth.log  ----> 读取的日志文件
          opslog            ----> 连接mongodb数据库名称呼
          auth              ----> 连接mongodb集合名称
          syslog            ----> 日志格式
