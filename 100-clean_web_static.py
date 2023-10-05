#!/usr/bin/python3
"""A Fabric script that deletes out-of-date archives"""

import os
from fabric.api import run, local, env, lcd, cd

env.hosts = ["100.27.3.38", "52.87.212.15"]
env.user = "ubuntu"


def do_clean(number=0):
    """clean the archieves"""

    number = int(number)
    if number == 0:
        number = 1
        print(number)

    archives = sorted(os.listdir("versions"))
    for i in range(number):
        archives.pop()
    with lcd("versions"):
        for arc in archives:
            local("rm {}".format(arc))

    with cd("/data/web_static/releases"):
        archieves = run("ls -tr").split()
        for arc in archieves:
            if "web_static_" in arc:
                archieves = arc
        archieves = list(archieves)
        for i in range(number):
            archieves.pop()
        for arc in archieves:
            run("rm -rf {}".format(arc))
