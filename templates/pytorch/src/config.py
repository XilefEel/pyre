from dataclasses import dataclass


@dataclass(frozen=True)
class TrainConfig:
    input_size: int = 8
    hidden_size: int = 64
    output_size: int = 1

    epochs: int = 20
    batch_size: int = 32
    learning_rate: float = 0.001

    checkpoint_dir: str = "checkpoints"
    save_every: int = 5
