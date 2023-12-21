#!/usr/bin/python3
'''
generates a tar archive
'''
from fabric.api import local
from datetime import datetime as dt


def do_pack():
    """packs the archive"""
    time = str(dt.now())
    now = time.split(".")[0]
    date_list = []
    full_date = now.split(" ")[0]
    for i in range(3):
        date_list.append(full_date.split("-")[i])
    year, month, day = date_list[0], date_list[1], date_list[2]
    full_time = now.split(" ")[1]
    time_list = []
    for i in range(3):
        time_list.append(full_time.split(":")[i])
    hour, minute, second = time_list[0], time_list[1], time_list[2]
    hms = f"{hour}{minute}{second}.tgz"
    file_name = f"versions/web_static_{year}{month}{day}" + hms
    result = local("mkdir -p versions")
    if result.return_code != 0:
        return None
    print(f"Packing web_static to {file_name}")
    local(f"tar -cvzf {file_name} web_static")
    if result.return_code == 0:
        return file_name
    else:
        return None
