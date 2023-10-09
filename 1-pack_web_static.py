#!/usr/bin/python3
"""Fabric script that compress contents of web_static dir"""


import os
from fabric.api import *
from datetime import datetime


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
