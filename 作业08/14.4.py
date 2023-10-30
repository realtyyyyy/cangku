from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 获取20 Newsgroups数据集
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# 创建一个TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 使用TF-IDF向量化器拟合并转换文本数据
tfidf_matrix = tfidf_vectorizer.fit_transform(newsgroups.data)

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, newsgroups.target, test_size=0.2, random_state=42)

# 创建朴素贝叶斯分类器
nb_classifier = MultinomialNB()

# 在训练集上拟合分类器
nb_classifier.fit(X_train, y_train)

# 在训练集上做出预测
train_predictions = nb_classifier.predict(X_train)

# 在测试集上做出预测
test_predictions = nb_classifier.predict(X_test)

# 计算训练集和测试集的分类准确度
train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)

print("训练集准确度:", train_accuracy)
print("测试集准确度:", test_accuracy)