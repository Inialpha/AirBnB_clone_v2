#!/usr/bin/python3
"""Creates .tgz file from the content of web_statuc directory and distributes
an archive to web servers, using the function do_deploy"""
from fabric.api import local, put, run, env
from datetime import datetime
import os.path

env.hosts = ["100.27.3.38", "52.87.212.15"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


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


def do_deploy(archive_path):
    """Fabric script that distributes an archive to web servers"""

    try:
        if not os.path.isfile(archive_path):
            return False
        put(archive_path, "/tmp/")
        file_name = os.path.basename(archive_path)
        release = "/data/web_static/releases/{}".format(file_name[:-4])
        run("rm -rf {}".format(release))
        run("mkdir -p {}".format(release))
        run("tar -xzf /tmp/{} -C {}".format(file_name, release))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(release, release))
        run("rm -rf {}/web_static/".format(release))
        run("rm -rf data/web_static/current")
        run("ln -sf {} {}".format(release, "/data/web_static/current"))
    except Exception:
        return False

    return True


def deploy():
    """Creates and distributes an archive to your web servers."""

    file_name = do_pack()
    if file_name is None:
        return False
    return do_deploy(file_name)
