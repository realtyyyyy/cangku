from sklearn.feature_extraction.text import CountVectorizer

# 示例文本
text_corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# 创建CountVectorizer对象
vectorizer = CountVectorizer()

# 将文本转换为词袋向量
X = vectorizer.fit_transform(text_corpus)

# 获取词袋模型中的特征词列表
feature_names = vectorizer.get_feature_names_out()

# 输出文本向量
print("文本向量:")
print(X.toarray())

# 输出特征词列表
print("特征词列表:")
print(feature_names)