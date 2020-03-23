# -*- coding:utf-8 -*-
"""
本程序基于train.sh,需传入4个参数：
    interval，执行训练的时间间隔，单位为“日”
    out，训练模型输出路径
    start_time，模型数据开始时间
    end_time，模型数据截止时间
topic、target、scene，从文件获取
"""
import os
import sys
import time

def run(train_file, interval, out, start_time, end_time):

    before_time = 0
    while True:
        try:
            local_time = time.time()
            # print(local_time)
            if local_time - before_time >= interval:
                train(train_file, out, start_time, end_time)
                before_time = local_time
        except Exception as e:
            print(e)
def train(train_file, out, start_time, end_time):
    with open(train_file, encoding='utf-8') as f:
        content = f.readlines()
        train_list = [c.replace('\n', '') for c in content]

    for row in train_list:
        [topic, target, scene] = row.split('|')
        command = 'sh train.sh' + ' ' + topic + ' ' + target + ' ' + scene + ' ' + \
                  out + ' ' + start_time + ' ' + end_time
        # 执行训练程序
        print('开始训练主题为%s，指标为%s，场景为%s的模型。。。'%(topic,target,scene))
        os.system(command)

if __name__ == "__main__":
    # 间隔时间为日
    interval = sys.argv[1]
    out = sys.argv[2]
    start_time = sys.argv[3]
    end_time = sys.argv[4]

    train_file = 'auto_train_list'
    interval = float(interval) * 24 * 3600

    run(train_file, interval, out, start_time, end_time)
