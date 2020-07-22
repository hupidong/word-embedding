#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
由原始文本进行分词后保存到新的文件
"""
import os
import sys
import jieba
import configparser

_WORK_DIR = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(_WORK_DIR, '../../common'))
import utils


def get_config(config_file='./config/config.ini'):
    parser = configparser.ConfigParser()
    parser.read(config_file)
    # get the ints, floats and strings
    _conf_segger = [(key, value) for key, value in parser.items('segger')]
    return dict(_conf_segger)


# 打印中文列表
def PrintListChinese(list):
    for i in range(len(list)):
        print(list[i])

    # 读取文件内容到列表

if __name__ == "__main__":
    seg_config = get_config(config_file='../config/config.ini')
    input_file_path = seg_config['segger_file_input_path']
    seg_file_save_path = seg_config['segger_file_save_path']

    fileTrainRead = []
    with open(input_file_path, 'r', encoding='utf8') as fileTrainRaw:
        for line in fileTrainRaw:  # 按行读取文件
            fileTrainRead.append(line)


    # jieba分词后保存在列表中
    fileTrainSeg = []
    for i in range(len(fileTrainRead)):
        # 9:-11索引，是因为语料中带有<content></content>标签
        fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i][9:-11], cut_all=False)))])
        percentage = int(i / len(fileTrainRead) * 100.0 + 0.5)
        utils.print_progress("Segger", percentage)

    # 保存分词结果到文件中
    with open(seg_file_save_path, 'w', encoding='utf-8') as fW:
        for i in range(len(fileTrainSeg)):
            fW.write(fileTrainSeg[i][0])
            fW.write('\n')