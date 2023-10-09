#!/usr/bin/python3
"""module that distributes and archive to remote servers"""


import os
from fabric.api import *


env.hosts = ['18.233.66.148', '54.236.184.219']


def do_deploy(archive_path):
    """function that deploys archive to remote servers"""

    if os.path.isfiile(archive_path) is False:
        return False

    dir = "/data/web_static/releases/"
    file = archive_path.split('/')[-1]
    fname = file.split('.')[0]
    put(archive_path, '/tmp/{}'.format(file))
    run("sudo tar -xf /tmp/{} -C {}/{}".format(file, dir, name))
    run("sudo rm /tmp/{}".format(file))
    run("sudo unlink /data/web_static/current")
    run("sudo ln -sf /data/web_static/releases/{} /data/web_static/current".
        format(name))
    return True
