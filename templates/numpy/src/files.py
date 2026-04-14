from pathlib import Path

import numpy as np
import pandas as pd
from result import Err, Ok, Result


def load_csv(path: Path) -> Result[pd.DataFrame, str]:
    try:
        df = pd.read_csv(path)
        return Ok(df)
    except FileNotFoundError:
        return Err(f"File not found: {path}")
    except Exception as e:
        return Err(f"Failed to load CSV: {e}")


def save_csv(df: pd.DataFrame, path: Path) -> Result[None, str]:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
        return Ok(None)
    except Exception as e:
        return Err(f"Failed to save CSV: {e}")


def load_npy(path: Path) -> Result[np.ndarray, str]:
    try:
        array = np.load(path)
        return Ok(array)
    except FileNotFoundError:
        return Err(f"File not found: {path}")
    except Exception as e:
        return Err(f"Failed to load npy: {e}")


def save_npy(array: np.ndarray, path: Path) -> Result[None, str]:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        np.save(path, array)
        return Ok(None)
    except Exception as e:
        return Err(f"Failed to save npy: {e}")
