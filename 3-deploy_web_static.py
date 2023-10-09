#!/usr/bin/python3
"""creates and distributes and achrive to remote servers"""


import os
from fabric.api import *
from datetime import datetime


env.hosts = ['18.233.66.148', '54.236.184.219']


def do_pack():
    """Generates a.tgz archive"""

    if os.path.isdir('./versions') is False:
        os.mkdir('./versions')

    cur = datetime.utcnow()
    fname = "web_static_{}{}{}{}{}{}.tgz".format(cur.year,
                                                 cur.month,
                                                 cur.day,
                                                 cur.hour,
                                                 cur.minute,
                                                 cur.second)
    local("tar czf {}  ./web_static".format(fname))
    local("mv {} ./versions".format(fname))
    return "versions/{}".format(fname)


def do_deploy(archive_path):
    """function that deploys archive to remote servers"""

    if os.path.isfile(archive_path) is False:
        return False

    dir = "/data/web_static/releases/"
    file = archive_path.split('/')[-1]
    fname = file.split('.')[0]
    put(archive_path, '/tmp/{}'.format(file))
    run("sudo tar -xf /tmp/{} -C {}/{}".format(file, dir, fname))
    run("sudo rm /tmp/{}".format(file))
    run("sudo unlink /data/web_static/current")
    run("sudo ln -sf /data/web_static/releases/{} /data/web_static/current".
        format(fname))
    return True


def deploy():
    """creates and distributes and achrive to remote servers"""

    file_path = do_pack()

    if os.path.isfile(file_path) is False:
        return False
    return do_deploy(file_path)
