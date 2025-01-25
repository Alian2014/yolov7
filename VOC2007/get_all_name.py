# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = ['train', 'val', 'test']
classes = set()
abs_path = os.getcwd()
print(abs_path)


def convert_annotation(image_id):
    in_file = open('E:/Learning/yolov7/VOC2007/Annotations/%s.xml' % (image_id), encoding='UTF-8')
    out_file = open('E:/Learning/yolov7/VOC2007/all_classes.txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    for obj in root.iter('object'):
        cls = obj.find('name').text
        classes.add(cls)
        out_file.write(', '.join(str(x) for x in classes))


if __name__ == '__main__':
    for image_set in sets:
        image_ids = open('E:/Learning/yolov7/VOC2007/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()

        for image_id in image_ids:
            convert_annotation(image_id)
