from pathlib import Path

import numpy as np
import pandas as pd
from result import Err, Ok

from analysis import get_column_stats, get_dataset_info, normalize
from data import save_csv


def main() -> None:
    print("Hello from {project_name}!\n")

    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie"],
            "age": [25, 30, 35],
            "score": [88.5, 92.0, 78.3],
        }
    )

    info = get_dataset_info(df)
    print(f"Dataset: {info.rows} rows, {info.columns} columns")
    print(f"Missing values: {info.missing_values}")
    print(f"Numeric columns: {info.numeric_columns}")

    stats = get_column_stats(df, "score")
    print("\nScore stats:")
    print(f"  Mean: {stats.mean:.2f}")
    print(f"  Std:  {stats.std:.2f}")
    print(f"  Min:  {stats.min:.2f}")
    print(f"  Max:  {stats.max:.2f}")

    scores = np.array(df["score"].values, dtype=np.float64)
    normalized = normalize(scores)
    print(f"\nRaw scores:        {scores}")
    print(f"Normalized scores: {normalized.round(2)}")

    match save_csv(df, Path("output/results.csv")):
        case Ok(_):
            print("\nResults saved to output/results.csv")
        case Err(e):
            print(f"\nFailed to save: {e}")


if __name__ == "__main__":
    main()
