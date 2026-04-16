from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from config import TrainConfig
from model import MLP


def train(model: MLP, config: TrainConfig) -> None:
    from dataset import DummyDataset

    dataset = DummyDataset(num_samples=1000, input_size=config.input_size)
    dataloader = DataLoader(dataset, batch_size=config.batch_size, shuffle=True)

    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)
    criterion = nn.MSELoss()

    checkpoint_dir = Path(config.checkpoint_dir)
    checkpoint_dir.mkdir(exist_ok=True)

    for epoch in range(1, config.epochs + 1):
        total_loss = 0.0

        for X, y in dataloader:
            optimizer.zero_grad()
            output = model(X)
            loss = criterion(output, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(dataloader)
        print(f"  Epoch {epoch:>3}/{config.epochs} — loss: {avg_loss:.4f}")

        if epoch % config.save_every == 0:
            checkpoint_path = checkpoint_dir / f"checkpoint_epoch_{epoch}.pt"
            torch.save(model.state_dict(), checkpoint_path)
            print(f"  Checkpoint saved to {checkpoint_path}")
