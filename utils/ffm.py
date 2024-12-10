import torch
import torch.nn as nn


class FieldAwareFactorizationMachine(nn.Module):
    def __init__(self, num_features, num_fields, latent_dim):
        super(FieldAwareFactorizationMachine, self).__init__()
        self.latent_dim = latent_dim
        self.num_fields = num_fields

        # Field-aware embedding
        self.embeddings = nn.ModuleList(
            [nn.Embedding(num_features, latent_dim) for _ in range(num_fields)]
        )

    def forward(self, x, field_indices):
        linear_part = torch.sum(x, dim=1)

        # Interaction term
        interaction_part = 0
        for i in range(self.num_fields):
            for j in range(i + 1, self.num_fields):
                v_i = self.embeddings[i](x[:, i])
                v_j = self.embeddings[j](x[:, j])
                interaction_part += torch.sum(v_i * v_j, dim=1)

        return linear_part + interaction_part