import pandas as pd
import matplotlib

# Use a non-interactive backend for headless environments
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from pathlib import Path


def ensure_reports_dir(base_dir: Path) -> Path:
    reports_dir = base_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    return reports_dir


def load_dataframe(data_dir: Path) -> pd.DataFrame:
    csv_path = data_dir / "train_Dataset_1.csv"
    return pd.read_csv(csv_path)


def to_float(series: pd.Series, pattern: str) -> pd.Series:
    """Extract numeric component using regex and convert to float."""
    extracted = series.astype(str).str.extract(pattern)[0]
    return pd.to_numeric(extracted, errors="coerce")


def save_hist(series: pd.Series, path: Path, title: str, xlabel: str) -> None:
    plt.figure()
    series.dropna().hist(bins=30)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def save_bar(counts: pd.Series, path: Path, title: str, xlabel: str) -> None:
    plt.figure()
    counts.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def main() -> None:
    base_dir = Path(__file__).resolve().parents[1]
    data_dir = base_dir / "data"
    reports_dir = ensure_reports_dir(base_dir)

    df = load_dataframe(data_dir)

    # Convert fields to numeric values without units
    df["Mileage_num"] = to_float(df["Mileage"], r"(\d+\.?\d*)")
    df["Engine_num"] = to_float(df["Engine"], r"(\d+)")
    df["Power_num"] = to_float(df["Power"], r"(\d+\.?\d*)")

    # Histograms
    save_hist(df["Mileage_num"], reports_dir / "mileage_hist.png", "Mileage Distribution", "Mileage")
    save_hist(df["Engine_num"], reports_dir / "engine_hist.png", "Engine Distribution", "Engine (cc)")
    save_hist(df["Power_num"], reports_dir / "power_hist.png", "Power Distribution", "Power")

    # Bar charts by category
    if "Fuel_Type" in df.columns:
        fuel_counts = df["Fuel_Type"].value_counts()
        save_bar(fuel_counts, reports_dir / "fueltype_count.png", "Cars per Fuel Type", "Fuel Type")

    if "Transmission" in df.columns:
        trans_counts = df["Transmission"].value_counts()
        save_bar(trans_counts, reports_dir / "transmission_count.png", "Cars per Transmission", "Transmission")


if __name__ == "__main__":
    main()
