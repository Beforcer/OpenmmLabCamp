# _base_ = [
#     '../configs/_base_/models/pspnet_r50-d8.py', '../configs/_base_/datasets/pascal_voc12.py',
#     '../configs/_base_/default_runtime.py', '../configs/_base_/schedules/schedule_40k.py'
# ]
_base_ = [
    '../configs/_base_/models/pspnet_r50-d8.py',
    '../configs/_base_/datasets/pascal_voc12.py',
    '../configs/_base_/default_runtime.py',
    '../configs/_base_/schedules/schedule_20k.py'
]
# norm_cfg = dict(type='BN', requires_grad=True)
# crop_size = (256, 256)
dataset_type = 'PascalVOCDataset'
# data_root = 'data/VOCdevkit/VOC2012'
data_root = '../datasets/VOCdevkit/VOC2012'
# data_root = '../datasets/Glomeruli-dataset/VOC'
model = dict(
    # pretrained=None,
    decode_head=dict(num_classes=21), auxiliary_head=dict(num_classes=21))

data = dict(
    samples_per_gpu=8,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        data_root=data_root,),
    val=dict(
        type=dataset_type,
        data_root=data_root,),
    test=dict(
        type=dataset_type,
        data_root=data_root,))

load_from = 'checkpoints/pspnet_r50b-d8_512x1024_80k_cityscapes_20201225_094315-6344287a.pth'
runner = dict(type='IterBasedRunner', max_iters=1000)
checkpoint_config = dict(by_epoch=False, interval=500)
evaluation = dict(interval=200, metric='mIoU', pre_eval=True)
log_config = dict(
    interval=100,
    )
# model = dict(
#     type='EncoderDecoder',
#     pretrained='open-mmlab://resnet50_v1c',
#     backbone=dict(
#         norm_cfg=norm_cfg,),
#     decode_head=dict(
#         num_classes=2,
#         norm_cfg=norm_cfg,),
#     auxiliary_head=dict(
#         num_classes=2,
#         norm_cfg=norm_cfg,),
#     # model training and testing settings
#     )

