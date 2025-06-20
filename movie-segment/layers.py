import torch
import torch.nn as nn
import torch.nn.functional as F

class GraphConvolution(nn.Module):
    def __init__(self, in_features, out_features, residual=False):
        super(GraphConvolution, self).__init__()
        self.linear = nn.Linear(in_features, out_features)
        self.residual = residual

    def forward(self, x, adj):
        adj = adj.unsqueeze(0).expand(x.shape[0], -1, -1)
        output = F.relu(self.linear(torch.matmul(adj, x)))

        if self.residual:
            output += x  

        return output

class SimilarityAdj(nn.Module):
    def __init__(self, in_features, out_features):
        super(SimilarityAdj, self).__init__()
        self.linear = nn.Linear(in_features, out_features)

    def forward(self, x):
        similarity = torch.matmul(x, x.transpose(-2, -1))
        return F.softmax(self.linear(similarity), dim=-1)
