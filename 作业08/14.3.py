from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

# 从sklearn中获取20 Newsgroups数据集
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# 创建一个TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 使用TF-IDF向量化器拟合并转换文本数据
tfidf_matrix = tfidf_vectorizer.fit_transform(newsgroups.data)

# 获取第一个文本的TF-IDF向量
first_text_tfidf_vector = tfidf_matrix[0]

# 将TF-IDF向量转换为密集数组
first_text_tfidf_vector_dense = first_text_tfidf_vector.toarray()

# 输出第一个文本的TF-IDF向量
print("第一个文本的TF-IDF向量:")
print(first_text_tfidf_vector_dense)