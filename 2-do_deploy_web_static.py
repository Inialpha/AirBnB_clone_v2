#!/usr/bin/python3
"""Fabric script that distributes an archive
to web servers, using the function do_deploy"""
from fabric.api import run, put, env
import os.path

env.hosts = ["100.27.3.38", "52.87.212.15"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


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
