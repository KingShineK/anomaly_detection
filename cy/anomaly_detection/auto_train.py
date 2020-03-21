# -*- coding:utf-8 -*-
"""
本程序基于train.sh
只需传入一个参数：interval，执行训练的时间间隔，单位为“日”
"""
import os
import sys
import time

def run(command,interval):

    before_time = time.time()
    while True:
        try:
            local_time = time.time()
            # print(local_time)
            if local_time - before_time >= interval:
                os.system(command)
                before_time = local_time
        except Exception as e:
            print(e)

if __name__ == "__main__":
    # 间隔时间为日
    interval = sys.argv[1]

    command = 'sh train.sh'
    interval = int(interval) * 24 * 3600
    # 刚开始的时候执行一次
    os.system(command)
    run(command,interval)
