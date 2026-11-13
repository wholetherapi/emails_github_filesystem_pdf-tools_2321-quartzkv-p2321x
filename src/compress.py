"""Low-rank key/value cache compression."""
import torch


def low_rank_project(tensor, rank):
    """Project the last dimension of `tensor` onto a rank-`rank` subspace."""
    u, s, vh = torch.linalg.svd(tensor.float(), full_matrices=False)
    return (u[:, :, :rank] * s[:, :rank].unsqueeze(-1)) @ vh[:, :rank, :]
