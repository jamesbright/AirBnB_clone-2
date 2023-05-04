#!/usr/bin/python3
"""
fabric file that uploads and distributes archive to web servers
"""

from os.path import exists
from fabric.api import put, run, env
env.hosts = ['52.86.31.49', '3.89.155.193']


def do_deploy(archive_path):
    """uploads and decompresses an archive to a web server"""
    if  exists(archive_path) is False:
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
