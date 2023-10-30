import dgl
import torch
import torch.nn as nn
import torch.optim as optim
import dgl.data
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 加载Cora数据集
dataset = dgl.data.CoraGraphDataset()
graph = dataset[0]

# 定义GCN模型
class GCN(nn.Module):
    def __init__(self, in_feats, hidden_size, num_classes):
        super(GCN, self).__init__()
        self.layers = nn.ModuleList([
            dgl.nn.GraphConv(in_feats, hidden_size),
            dgl.nn.GraphConv(hidden_size, num_classes)
        ])

    def forward(self, g, features):
        x = features
        for layer in self.layers:
            x = layer(g, x)
        return x

# 设置随机种子以确保可重复性
torch.manual_seed(0)

# 定义超参数
in_feats = dataset.num_features
hidden_size = 16
num_classes = dataset.num_classes
lr = 0.01
epochs = 100

# 创建GCN模型
model = GCN(in_feats, hidden_size, num_classes)

# 创建优化器
optimizer = optim.Adam(model.parameters(), lr=lr)

# 损失函数
criterion = nn.CrossEntropyLoss()

# 训练循环
for epoch in range(epochs):
    model.train()
    logits = model(graph, graph.ndata['feat'])
    labels = graph.ndata['label']
    loss = criterion(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(f'Epoch [{epoch + 1}/{epochs}] Loss: {loss.item()}')

# 模型评估
model.eval()
with torch.no_grad():
    logits = model(graph, graph.ndata['feat'])
    _, predicted = logits.max(1)
    accuracy = (predicted == labels).sum().item() / len(labels)
    print(f'Accuracy: {accuracy * 100:.2f}%')
# 获取GCN模型的输出
model.eval()
with torch.no_grad():
    logits = model(graph, graph.ndata['feat'])

# 获取节点的特征和标签
features = logits.numpy()
labels = graph.ndata['label'].numpy()

# 使用PCA进行降维，将高维特征降至2维
pca = PCA(n_components=2)
features_2d = pca.fit_transform(features)

# 可视化降维后的结果
scatter = plt.scatter(features_2d[:, 0], features_2d[:, 1], c=labels, cmap='jet')
plt.legend(*scatter.legend_elements(), title='Classes')
plt.title('PCA Visualization of Cora Dataset')
plt.show()