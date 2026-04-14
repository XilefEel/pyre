import numpy as np
import pandas as pd
from result import Err, Ok, Result

from models import ColumnStats, DatasetInfo


def get_dataset_info(df: pd.DataFrame) -> DatasetInfo:
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_columns = df.select_dtypes(exclude=[np.number]).columns.tolist()

    return DatasetInfo(
        rows=len(df),
        columns=len(df.columns),
        missing_values=int(df.isnull().sum().sum()),
        numeric_columns=numeric_columns,
        categorical_columns=categorical_columns,
    )


def get_column_stats(df: pd.DataFrame, column: str) -> Result[ColumnStats, str]:
    if column not in df.columns:
        return Err(f"Column '{column}' not found.")

    series = df[column].dropna()

    if not pd.api.types.is_numeric_dtype(series):
        return Err(f"Column '{column}' is not numeric.")

    if series.empty:
        return Err(f"Column '{column}' is empty or contains only missing values.")

    return Ok(
        ColumnStats(
            name=column,
            mean=float(series.mean()),
            std=float(series.std()),
            min=float(series.min()),
            max=float(series.max()),
        )
    )


def normalize(array: np.ndarray) -> np.ndarray:
    min_val = float(array.min())
    max_val = float(array.max())
    if max_val == min_val:
        return np.zeros_like(array, dtype=np.float64)

    return (array - min_val) / (max_val - min_val)


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=[np.number]).corr()
