# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:15:14 2019

@author: Xiujie
"""
import os
import numpy as np
import json
from PIL import Image
import cv2


base_path = "./datas/train/jinnan2_round1_train_20190305/normal/"
for _,__,negative_samples in os.walk(base_path):
    break

f = open('train.txt','a+')
for sample in negative_samples[0:1000]:
    f.write(base_path + str(sample) + ' \n')
f.close()

'''
f = open('submit.JSON','r')
json_file = json.load(f)
print(json_file['results'][0])
'''

'''
显示json标注的结果
test_path = "./datas/test/jinnan2_round1_test_a_20190306/"

f = open('submit.Json','r')

json_file = f.readline()
json_dic = json.loads(json_file)

all_info = json_dic["results"][90:110]
for info in all_info:
    pic_path = test_path + info['filename']
    print(pic_path)
    image = cv2.imread(pic_path)
    if (len(info['rects']) == 0):
        image_arr = np.asarray(image,dtype=np.uint8)
        img = Image.fromarray(image_arr)
        img.show()
        continue
    else:
        for rect in info['rects']:
            image = cv2.rectangle(image,(rect['xmin'],rect['ymin']),\
                                  (rect['xmax'],rect['ymax']),(255, 0, 0), 2)
        image_arr = np.asarray(image,dtype=np.uint8)
        img = Image.fromarray(image_arr)
        img.show()
    
'''

'''
实现label +1
f = open('submit.JSON','r')
f2 = open('test.JSON','w')
file = f.readline()
json_ = json.loads(file)
json_file = json.dumps(json_)
f2.writelines(json_file)
f2.close()
'''



'''
f = open('submit.Json','r')
f2 = open('test.JSON','w')
json_file = f.readline()
json_dic = json.loads(json_file)

all_info = json_dic["results"]
for info in all_info:
    if (len(info['rects']) == 0):
        continue
    else:
        for rect in info['rects']:
           rect['label'] = rect['label'] + 1
json_ = json.dumps(json_dic)
f2.write(json_)
f2.close()
'''

'''
json_path = "./datas/train/jinnan2_round1_train_20190305/train_no_poly.json"
j = open(json_path,'r')
json_file = j.readline()
json_file = json.loads(json_file)
print(json_file['categories'])
'''