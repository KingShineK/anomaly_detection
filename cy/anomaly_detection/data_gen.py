import pandas as pd
import time
import random
import sys,os
import utils
import struct
import happybase

"""
python hbase_test.py --topic --target --scence --out --start_time --end_time
Example:
    python hbase_test.py www.cy.com pv count models/pv/ 2020-03-10 2020-03-14
"""
if __name__ == '__main__':

    host = '10.128.37.103'
    port = 6004

    con = happybase.Connection(host=host,port=port,protocol='compact',transport='framed')
    con.open()
    t = con.table('ai')

    topic = sys.argv[1]
    target = sys.argv[2]
    scene = sys.argv[3]
    start_time = sys.argv[4]
    end_time = sys.argv[5]
    # 起止时间补足时分秒，默认开始时间为当天日期00:00:00，终止时间为当天日期23:59:59
    start_time = start_time + "_00:00:00"
    end_time = end_time + "_23:59:59"

    save_name = 'data/' + scene + '/data'
    if os.path.exists(save_name):
        os.remove(save_name)
    res = '' # 存储所需字段
    cnt = 1 # 计数
    flag = True
    row_prefix = (topic + '|' + target + '|' + scene).encode('utf-8')
    for row in t.scan(row_prefix=row_prefix):
        try:
            rowKey = row[0].decode('utf-8')
            print(rowKey)
            timestamp = row[1][b'data:timestamp']
            timestamp = int(struct.unpack(">Q",timestamp)[0]/1000)

            value = row[1][b'data:value']
            value = struct.unpack(">Q",value)[0]
            ratio = row[1][b'data:ratio']
            ratio = struct.unpack(">Q",ratio)[0]

            if timestamp > end_time:
                if flag:
                    print("没有找到在该时间段内满足条件的数据！")
                break

            if timestamp >= start_time:
                flag = False
                if scene == 'count':
                    res = str(timestamp) + ',' + str(value) + '\n'
                    with open(save_name, 'a', encoding='utf8') as f:
                        f.write(res)
                    print('已保存%d条数据' % cnt)
                    cnt += 1
                elif scene == 'number':
                    res = str(timestamp) + ',' + str(value) + '\n'
                    with open(save_name, 'a', encoding='utf8') as f:
                        f.write(res)
                    print('已保存%d条数据' % cnt)
                    cnt += 1
                elif scene == 'ratio':
                    res = str(timestamp) + ',' + str(value) + ',' + str(ratio) + '\n'
                    with open(save_name, 'a', encoding='utf8') as f:
                        f.write(res)
                    print('已保存%d条数据' % cnt)
                    cnt += 1
        except Exception:
            print('数据提取发生错误：{}'.format(row))

    print('训练数据导出完成！')

    con.close()
