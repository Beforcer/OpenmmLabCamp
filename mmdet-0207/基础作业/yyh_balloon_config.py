_base_ = [
    '../configs/_base_/models/mask_rcnn_r50_fpn.py',
    '../configs/_base_/datasets/coco_instance.py',
    '../configs/_base_/schedules/schedule_1x.py',
    '../configs/_base_/default_runtime.py'
]
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))
dataset_type = 'CocoDataset'
classes = ('balloon',)
data = dict(
    train=dict(
        ann_file='../datasets/balloon/train/train_coco.json',
        img_prefix='../datasets/balloon/train/',
        classes=classes),
    val=dict(
        ann_file='../datasets/balloon/val/val_coco.json',
        img_prefix='../datasets/balloon/val/',
        classes=classes),
    test=dict(
        ann_file='../datasets/balloon/val/val_coco.json',
        img_prefix='../datasets/balloon/val/',
        classes=classes))

load_from = 'checkpoints/mask_rcnn_r50_fpn_1x_coco_20200205-d4b0c5d6.pth'