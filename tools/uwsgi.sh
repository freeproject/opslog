touch /tmp/opslog
. /opt/pyenv/bin/activate
cd /opt/project/opslog
uwsgi -s /tmp/uwsgi.sock \
-w main:app \
-H /opt/pyenv \
--listen 100 \
--buffer-size 32768 \
--max-requests 2000 \
--workers 4 \
--enable-threads \
--limit-as 256 \
--reload-on-as 256 \
--daemonize /tmp/opslog.log \
--pidfile /tmp/opslog.pid \
--touch-reload /tmp/opslog \
--chmod-socket 666

