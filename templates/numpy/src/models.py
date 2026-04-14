from dataclasses import dataclass


@dataclass(frozen=True)
class DatasetInfo:
    rows: int
    columns: int
    missing_values: int
    numeric_columns: list[str]
    categorical_columns: list[str]


@dataclass(frozen=True)
class ColumnStats:
    name: str
    mean: float
    std: float
    min: float
    max: float
