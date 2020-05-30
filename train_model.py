# -*- coding:utf8 -*-
# 引入 word2vec
from gensim.models import word2vec
# 引入日志配置
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 引入外部数据集
sentences = word2vec.LineSentence('/Users/greta/workspace/PythonProject/w2v-model_0428/data/all_cor.txt')

# 构建模型
model = word2vec.Word2Vec(sentences, min_count=5,size=300)

# 保存模型
model.save('./model/res_w2v.model')
model.wv.save_word2vec_format("./model/res_w2v.model.bin",binary=False)