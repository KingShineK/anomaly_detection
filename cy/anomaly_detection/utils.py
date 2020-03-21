# -*- coding:utf-8 -*-
import time

# 时间格式：'2019-8-01_00:00:00'
def time_to_timestamp(time_sj):
    data_sj = time.strptime(time_sj, "%Y-%m-%d_%H:%M:%S")
    time_int = int(time.mktime(data_sj))
    return time_int

def timestamp_to_time(timestamp):
    data_sj = time.localtime(timestamp)
    time_str = time.strftime("%Y-%m-%d_%H:%M:%S", data_sj)
    return time_str

if __name__ == '__main__':
    time1 = "2020-03-10_20:12:00"
    time2 = "2020-03-10_20:16:00"
    print(time_to_timestamp(time1))
    print(time_to_timestamp(time2))