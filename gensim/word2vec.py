# coding=utf8
"""
gensim word2vec获取词向量
"""

import configparser
import warnings
import logging
import os.path
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# 忽略警告
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

def get_config(config_file='./config/config.ini'):
    parser = configparser.ConfigParser()
    parser.read(config_file)
    _conf_word2vec = [(key, value) for key, value in parser.items('word2vec')]
    return dict(_conf_word2vec)

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])  # 读取当前文件的文件名
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # input_corpus_path为输入语料, out_model为输出模型, out_vector为vector格式的模型
    gconfig = get_config(config_file='config/config.ini')
    seggered_corpus_path = gconfig['word2vec_corpus_input_path']
    out_model = gconfig['word2vec_out_model_save_path']
    out_vector = gconfig['word2vec_out_vector_save_path']

    vector_size = int(gconfig['vec_size'])
    window_size = int(gconfig['window_size'])
    min_count = int(gconfig['min_count'])
    epoch_num = int(gconfig['epoch_num'])
    # 训练skip-gram模型
    model = Word2Vec(LineSentence(seggered_corpus_path), size=vector_size, window=window_size, min_count=min_count,
                     iter=epoch_num, workers=multiprocessing.cpu_count())

    # 保存模型
    model.save(out_model)
    # 保存词向量
    model.wv.save_word2vec_format(out_vector, binary=False)
