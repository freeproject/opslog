# 自动化部署
参考: tools/setup.py

# mongodo环境部署
参考: tools/init_db.py

# flask环境部署
    pip install virtualenv
    virtualenv /usr/local/venv
    . /usr/local/venv/bin/activate
    pip install Flask Flask-MongoAlchemy
    pip install uwsgi

# nginx环境部署
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
            server_name  10.0.25.3;
        root /data/project/opslog/static;
            location / { 
            include uwsgi_params; 
            uwsgi_pass unix:/tmp/uwsgi.sock; 
            }
        }
    }
    EOF

# 客户端部署
参考：tools/tailflog.py

例子：

    python /admin/tailflog.py /var/log/auth.log opslog auth syslog
    参数：/var/log/auth.log  ----> 读取的日志文件
          opslog            ----> 连接mongodb数据库名称呼
          auth              ----> 连接mongodb集合名称
          syslog            ----> 日志格式
