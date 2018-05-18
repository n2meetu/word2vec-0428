import gensim

newModel = gensim.models.Word2Vec.load("./model/res_w2v.model")

# 计算两个词之间的余弦距离
def distance(word1,word2):
    y2 = newModel.similarity(word1,word2)  # 计算两个词之间的余弦距离
    y2 = float('%.2f' % y2)
    print(word1, word2,y2)

# 计算余弦距离最接近word的10个词：
def synonyms(word):
    print('\n计算余弦距离最接近“'+word+'”的10个词：')
    # 余弦值的范围在[-1, 1]之间，值越趋近于1，代表两个向量的方向越接近；越趋近于 - 1，他们的方向越相反；接近于0，表示两个向量近乎于正交。
    for i in newModel.most_similar(word):
        print(i[0], float('%.2f' % i[1]))

result = newModel.similarity('还行', '不错')
result2 = newModel.similarity('可口', '好喝')
print(result,result2)

print(synonyms('放心'))