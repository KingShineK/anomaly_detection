# -*- coding:utf-8 -*-
"""
本程序基于train.sh,需传入7个参数：
    interval，执行训练的时间间隔，单位为“日”
    topic，对应 kafka 的 topic
    target，指标
    scene，场景
    out，训练模型输出路径
    start_time，模型数据开始时间
    end_time，模型数据截止时间
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
    topic = sys.argv[2]
    target = sys.argv[3]
    scene = sys.argv[4]
    out = sys.argv[5]
    start_time = sys.argv[6]
    end_time = sys.argv[7]

    command = 'sh train.sh' + ' ' + topic + ' ' + target + ' ' + scene + ' ' + \
              out + ' ' + start_time + ' ' + end_time
    interval = int(interval) * 24 * 3600
    # 刚开始的时候执行一次
    os.system(command)
    run(command, interval)
