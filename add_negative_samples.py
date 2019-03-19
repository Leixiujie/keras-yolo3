# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:15:14 2019

@author: Xiujie
"""
import os
import json

base_path = "./datas/train/jinnan2_round1_train_20190305/normal/"
for _,__,negative_samples in os.walk(base_path):
    break

f = open('train.txt','a+')
for sample in negative_samples[1000:2000]:
    f.write(base_path + str(sample) + ' \n')
f.close()
'''
f = open('submit.JSON','r')
json_file = json.load(f)
print(json_file['results'][0])
'''