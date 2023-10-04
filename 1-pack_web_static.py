#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os.path

"""Creates a .tgz file from the content of web_statuc directory"""


def do_pack():
    """generates a .tgx file"""
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_" + time + ".tgz"
    if os.path.isdir("versions") is False:
        local("mkdir versions")

    stat = local("tar -cvzf {} web_static".format(name))
    if stat.succeeded:
        return name
    else:
        return None
