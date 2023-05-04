#!/usr/bin/python3
"""
fabric file that uploads and distributes archive to web servers
"""

import os.path
from fabric.api import put, run, env, local
from datetime import datetime
from os.path import isdir
env.hosts = ['52.86.31.49', '3.89.155.193']


def do_pack():
    """generates a tgz archive from folders"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """uploads and decompresses an archive to a web server"""
    if not os.path.isfile(archive_path):
        return False
    try:
        archive = archive_path.split("/")[-1]
        rm_ext = archive_path.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, rm_ext))
        run('tar -xzf  /tmp/{} -C {}{}/'.format(archive, path, rm_ext))
        run('rm /tmp/{}'.format(archive))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, rm_ext))
        run('rm -rf {}{}/web_static'.format(path, rm_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, rm_ext))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
