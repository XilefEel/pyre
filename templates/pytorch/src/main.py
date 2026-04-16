import torch

from config import TrainConfig
from model import MLP
from train import train


def main() -> None:
    print("Hello from {project_name}!\n")

    config = TrainConfig()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"  Device: {device}")
    print(f"  Epochs: {config.epochs}")
    print(f"  Batch size: {config.batch_size}")
    print(f"  Learning rate: {config.learning_rate}\n")

    model = MLP(
        input_size=config.input_size,
        hidden_size=config.hidden_size,
        output_size=config.output_size,
    ).to(device)

    print("Training...\n")
    train(model, config)
    print("\nDone!")


if __name__ == "__main__":
    main()
