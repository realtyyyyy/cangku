from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

import requests
from bs4 import BeautifulSoup

# 发送GET请求获取网页内容
url = "http://www.cs.cmu.edu/afs/cs/project/theo-11/www/naive-bayes.html"
response = requests.get(url)

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 提取文本数据和标签
texts = []
labels = []

# 通过查找HTML元素或CSS类来定位文本和标签
# 例如，如果文本在<p>标签内，标签在<span>标签内：
for p_tag in soup.find_all('p'):
    text = p_tag.get_text()
    label = p_tag.find('span').get_text()
    texts.append(text)
    labels.append(label)

tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # 使用TF-IDF向量化
X = tfidf_vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

nb_classifier = MultinomialNB()
nb_classifier.fit(X_train, y_train)

y_pred = nb_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("准确度:", accuracy)