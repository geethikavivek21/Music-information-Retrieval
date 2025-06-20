import torch
import torch.nn as nn
import torch.nn.init as torch_init
from layers import GraphConvolution, SimilarityAdj

class Model(nn.Module):
    def __init__(self, args):
        super(Model, self).__init__()
        self.gc1 = GraphConvolution(128, 32, residual=True)
        self.gc2 = GraphConvolution(32, 32, residual=True)
        self.similarity_adj = SimilarityAdj(128, 32)
        self.fc = nn.Linear(32, args.num_classes)
        self.apply(self.weight_init)

    def weight_init(self, m):
        if hasattr(m, 'weight') and isinstance(m, nn.Linear):
            torch_init.xavier_uniform_(m.weight)

    def forward(self, x, adj):
        adj = self.similarity_adj(x)
        x = self.gc1(x, adj)
        x = self.gc2(x, adj)
        x = torch.mean(x, dim=1)
        return self.fc(x)
