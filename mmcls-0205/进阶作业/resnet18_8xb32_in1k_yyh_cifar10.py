_base_ = [
    'configs/_base_/models/resnet18.py',
    'configs/_base_/datasets/cifar10_bs16.py',
    'configs/_base_/schedules/imagenet_bs256.py',
    'configs/_base_/default_runtime.py'
]
model = dict(
    head=dict(
        topk=(1,)))
data = dict(
    train=dict(
        data_prefix='../datasets/cifar10',  # 修改为自定义数据集路径
    ),
    val=dict(
        data_prefix='../datasets/cifar10',  # 修改为自定义数据集路径
        ),
    test=dict(
        data_prefix='../datasets/cifar10',  # 修改为自定义数据集路径
        )
)
optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001)
runner = dict(type='EpochBasedRunner', max_epochs=50)
checkpoint_config = dict(interval=5)  # 设置多少个epochs 存储一次模型
log_config = dict(interval=1000, hooks=[dict(type='TextLoggerHook')])
load_from = 'resnet18_8xb32_in1k_20210831-fbbb1da6.pth'  # 写入预训练模型