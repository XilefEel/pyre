import torch
from torch.utils.data import Dataset


class DummyDataset(Dataset[tuple[torch.Tensor, torch.Tensor]]):
    def __init__(self, num_samples: int, input_size: int) -> None:
        self.X = torch.randn(num_samples, input_size)
        self.y = self.X.sum(dim=1, keepdim=True)

    def __len__(self) -> int:
        return len(self.X)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        return self.X[idx], self.y[idx]
