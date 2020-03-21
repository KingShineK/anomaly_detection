#!/bin/bash

topic=$1
target=$2
scene=$3
out=$4
start_time=$5
end_time=$6

echo "开始生成训练集~"
python3 data_gen.py ${topic} ${target} ${scene} ${start_time} ${end_time}
echo "训练集生成完毕！"
path=$out"/"$topic"_"$target
if [ ! -d $path ];then
    echo "模型目录不存在，可以创建"
else
    rm -rf $path
    echo "模型目录已存在，已删除"

fi
mkdir -p $path
echo "模型目录已创建，开始训练模型。。。"
sh anomaly_detection_train/demo.sh ${scene} ${path}
echo "模型训练完成！保存路径："$path

echo "开始同步中。。。"
rsync -avzP /home/models/ --delete --password-file=/etc/rsync.password model@10.128.37.194::model
if [ $? -eq 0 ]; then
    echo "训练模型同步到10.128.37.194成功！"
else
    echo "训练模型同步到10.128.37.194失败！"
fi

rsync -avzP /home/models/ --delete --password-file=/etc/rsync.password model@10.128.37.62::model
if [ $? -eq 0 ]; then
    echo "训练模型同步到10.128.37.62成功！"
else
    echo "训练模型同步到10.128.37.62失败！"
fi

rsync -avzP /home/models/ --delete --password-file=/etc/rsync.password model@10.128.36.161::model
if [ $? -eq 0 ]; then
    echo "训练模型同步到10.128.36.161成功！"
else
    echo "训练模型同步到10.128.36.161失败！"
fi

rsync -avzP /home/models/ --delete --password-file=/etc/rsync.password model@10.128.36.192::model
if [ $? -eq 0 ]; then
    echo "训练模型同步到10.128.36.192成功！"
else
    echo "训练模型同步到10.128.36.192失败！"
fi

rsync -avzP /home/models/ --delete --password-file=/etc/rsync.password model@10.128.36.227::model
if [ $? -eq 0 ]; then
    echo "训练模型同步到10.128.36.227成功！"
else
    echo "训练模型同步到10.128.36.227失败！"
fi

rsync -avzP /home/models/ --delete --password-file=/etc/rsync.password model@10.128.36.182::model
if [ $? -eq 0 ]; then
    echo "训练模型同步到10.128.36.182成功！"
else
    echo "训练模型同步到10.128.36.182失败！"
fi
