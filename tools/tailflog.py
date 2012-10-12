#!/usr/bin/env python
#coding=utf-8

from pymongo import Connection
from datetime import datetime
from time import sleep
import sys, os
import re


""" Usage: python /admin/tailflog.py /var/log/syslog dbname colname syslog """

connection = Connection('localhost', 27017)
db = connection['%s' % sys.argv[2]]
collection = db['%s' % sys.argv[3]]
logformat = sys.argv[4]

syslog = re.compile('(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(.[^ ]+)\s+(\S+):\s+(.*)')
weblog = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\[(\S+).*\]')
year = datetime.now().year


def daemonize(pidfile='/dev/null', stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    # Do first fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)   # Exit first parent.
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)

    # Decouple from parent environment.
    os.chdir("/")
    os.umask(0)
    os.setsid()

    # Do second fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)   # Exit second parent.
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)

    # Now I am a daemon!
    # Redirect standard file descriptors.
    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    # write pidfile
    pid = str(os.getpid())
    file(pidfile, 'w+').write("%s\n" % pid)


def tail_f(file):
    interval = 1.0

    while True:
        where = file.tell()
        line = file.readline()
        if not line:
            sleep(interval)
            file.seek(where)
        else:
            yield line


def main():
    if logformat == 'nginx':
        for line in tail_f(open(sys.argv[1])):
            print weblog.search(line).group(2)

    elif logformat == 'syslog':
        for line in tail_f(open(sys.argv[1])):
            print line
            post = [{
            #'time': datetime.strptime(syslog.match(line).group(1), "%b %d %H:%M:%S").utcnow(),
            'time': datetime.strptime("%s %s" % (year,
                                                 syslog.match(line).group(1)),
                                                 "%Y %b %d %H:%M:%S"),
            'host': syslog.match(line).group(2),
            'ident': syslog.match(line).group(3),
            'message': syslog.match(line).group(4),
            }]
            collection.insert(post)
    else:
        sys.exit(1)


def test():
    if logformat == 'nginx':
        for line in tail_f(open(sys.argv[1])):
            print weblog.search(line).group(2)

    elif logformat == 'syslog':
        for line in tail_f(open(sys.argv[1])):
            print syslog.match(line).group(1)
            post = [{
            'time': datetime.strptime("%s %s" % (year,
                                                 syslog.match(line).group(1)),
                                                 "%Y %b %d %H:%M:%S"),
            'host': syslog.match(line).group(2),
            'ident': syslog.match(line).group(3),
            'message': syslog.match(line).group(4),
            }]
            #print line
            print post[0]['time']
            print post[0]['host']
            print post[0]['ident']
            print post[0]['message']

    else:
        sys.exit(1)


if __name__ == "__main__":
    daemonize('/tmp/%s.pid' % collection.name,
              '/dev/null',
              '/tmp/%s.log' % collection.name,
              '/tmp/%s.err' % collection.name)
    main()
