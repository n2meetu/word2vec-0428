# -*- coding:utf8 -*-
# 把12个评论文档全部合在一起，用jieba进行分词
import os
import jieba
import random
corpus_path = '/Users/greta/workspace/PythonProject/w2v-model_0427/data/corpus/'


def get_corpus_path(path):
    return os.path.join(corpus_path, path)



def get_corpus_path(path):
    return os.path.join(corpus_path, path)


def cut_sent_list(sent_list):
    return list(map(lambda x: ' '.join(jieba.cut(x)), sent_list))

def append_dict(corpus, sent_list):
    for line in sent_list:
        line  = line.strip(' ')
        line = line.replace('、', ' ')
        line = line.replace('.', ' ')
        line = line.replace('!', ' ')
        line = line.replace('！', ' ')
        line = line.replace('，', ' ')
        line = line.replace(',', ' ')
        line = line.replace('。', ' ')
        line = line.replace('~', ' ')
        line = line.replace('～', ' ')
        line = line.replace('{"error_message": "EMPTY SENTENCE"}', ' ')
        line = line.replace('…', ' ')
        line = line.replace('\r', '')
        line = line.replace('\t', ' ')
        line = line.replace('\f', ' ')
        line = line.replace('/', ' ')
        line = line.replace('.......', ' ')
        line = line.replace('、', ' ')
        line = line.replace('/', ' ')
        line = line.replace(' ', ' ')
        line = line.replace(' ', ' ')
        line = line.replace('_', ' ')
        line = line.replace('?', ' ')
        line = line.replace('？', ' ')
        # line = line.replace('了', '')
        line = line.replace('➕', ' ')
        corpus.append(line)

if __name__ == '__main__':
    corpus = []
    food_pos = cut_sent_list(open(get_corpus_path('food_pos.txt')).readlines())
    food_neu = cut_sent_list(open(get_corpus_path('food_neu.txt')).readlines())
    food_neg = cut_sent_list(open(get_corpus_path('food_neg.txt')).readlines())
    env_pos = cut_sent_list(open(get_corpus_path('env_pos.txt')).readlines())
    env_neu = cut_sent_list(open(get_corpus_path('env_neu.txt')).readlines())
    env_neg = cut_sent_list(open(get_corpus_path('env_neg.txt')).readlines())
    price_pos = cut_sent_list(open(get_corpus_path('price_pos.txt')).readlines())
    price_neu = cut_sent_list(open(get_corpus_path('price_neu.txt')).readlines())
    price_neg = cut_sent_list(open(get_corpus_path('price_neg.txt')).readlines())
    ser_pos = cut_sent_list(open(get_corpus_path('ser_pos.txt')).readlines())
    ser_neu = cut_sent_list(open(get_corpus_path('ser_neu.txt')).readlines())
    ser_neg = cut_sent_list(open(get_corpus_path('ser_neg.txt')).readlines())

    append_dict(corpus, food_pos)
    append_dict(corpus, food_neu)
    append_dict(corpus, food_neg)
    append_dict(corpus, env_pos)
    append_dict(corpus, env_neu)
    append_dict(corpus, env_neg)
    append_dict(corpus, price_pos)
    append_dict(corpus, price_neu)
    append_dict(corpus, price_neg)
    append_dict(corpus, ser_pos)
    append_dict(corpus, ser_neu)
    append_dict(corpus, ser_neg)

    random.shuffle(corpus)
    # print("all's length:\n",len(corpus))

    all_cor = open('./data/all_cor.txt','w')

    for line in corpus:
        all_cor.write(line)




