_base_ = [
    '../configs/_base_/models/faster_rcnn_r50_fpn.py', '../configs/_base_/datasets/voc0712.py',
    '../configs/_base_/default_runtime.py'
]

model = dict(
    backbone=dict(
        init_cfg=None),
    roi_head=dict(bbox_head=dict(num_classes=20)))
data_root = '../datasets/VOCdevkit/'
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=2,
    train=dict(
        dataset=dict(
            ann_file=[
                data_root + 'VOC2007/ImageSets/Main/train.txt',
                data_root + 'VOC2012/ImageSets/Main/train.txt'
            ],
            img_prefix=[data_root + 'VOC2007/', data_root + 'VOC2012/'],
            )),
    val=dict(
        ann_file=data_root + 'VOC2007/ImageSets/Main/val.txt',
        img_prefix=data_root + 'VOC2007/',
        ),
    test=dict(
        ann_file=data_root + 'VOC2007/ImageSets/Main/val.txt',
        img_prefix=data_root + 'VOC2007/',
        ))
# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
# actual epoch = 3 * 3 = 9
lr_config = dict(policy='step', step=[3])
load_from = 'checkpoints/faster_rcnn_r50_fpn_1x_voc0712_20220320_192712-54bef0f3.pth'
# runtime settings
runner = dict(
    type='EpochBasedRunner', max_epochs=4)  # actual epoch = 4 * 3 = 12