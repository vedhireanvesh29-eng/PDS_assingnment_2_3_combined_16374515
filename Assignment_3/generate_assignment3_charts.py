import pandas as pd
import numpy as np
import matplotlib

# Use non-interactive backend
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from pathlib import Path


def ensure_reports_dir(base_dir: Path) -> Path:
    reports_dir = base_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    return reports_dir


def load_diabetes_df(data_dir: Path) -> pd.DataFrame:
    preferred = data_dir / "diabetes.csv"
    fallback = data_dir / "diabetes_Dataset_2.csv"

    if preferred.exists():
        return pd.read_csv(preferred)
    if fallback.exists():
        print("diabetes.csv not found. Using diabetes_Dataset_2.csv instead.")
        return pd.read_csv(fallback)
    raise FileNotFoundError("Neither diabetes.csv nor diabetes_Dataset_2.csv found in data/.")


def bar_chart(values, labels, path: Path, title: str, ylabel: str) -> None:
    plt.figure()
    plt.bar(labels, values, color=["#4C78A8", "#F58518"])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def histogram(data, path: Path, title: str, xlabel: str) -> None:
    plt.figure()
    plt.hist(data, bins=30)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def main() -> None:
    base_dir = Path(__file__).resolve().parents[1]
    data_dir = base_dir / "data"
    reports_dir = ensure_reports_dir(base_dir)

    df = load_diabetes_df(data_dir)

    sample = df.sample(25, random_state=42)

    sample_mean_glucose = sample["Glucose"].dropna().mean()
    pop_mean_glucose = df["Glucose"].dropna().mean()
    sample_max_glucose = sample["Glucose"].dropna().max()
    pop_max_glucose = df["Glucose"].dropna().max()

    sample_bmi_98 = np.percentile(sample["BMI"].dropna(), 98)
    pop_bmi_98 = np.percentile(df["BMI"].dropna(), 98)

    bootstrap_means = []
    for _ in range(500):
        boot = df.sample(150, replace=True)
        bootstrap_means.append(boot["BloodPressure"].mean())

    bootstrap_avg_bp = float(np.mean(bootstrap_means))
    population_bp_mean = float(df["BloodPressure"].dropna().mean())

    # Charts for glucose stats
    bar_chart(
        [sample_mean_glucose, pop_mean_glucose],
        ["Sample", "Population"],
        reports_dir / "sample_vs_pop_mean_glucose.png",
        "Sample vs Population Mean Glucose",
        "Mean Glucose",
    )

    bar_chart(
        [sample_max_glucose, pop_max_glucose],
        ["Sample", "Population"],
        reports_dir / "sample_vs_pop_max_glucose.png",
        "Sample vs Population Max Glucose",
        "Max Glucose",
    )

    # BMI percentiles
    bar_chart(
        [sample_bmi_98, pop_bmi_98],
        ["Sample 98th", "Population 98th"],
        reports_dir / "sample_vs_pop_98th_bmi.png",
        "Sample vs Population 98th Percentile BMI",
        "BMI",
    )

    # Bootstrap hist and comparison bar
    histogram(bootstrap_means, reports_dir / "bootstrap_bp_hist.png", "Bootstrap Mean Blood Pressure", "Mean BP")

    bar_chart(
        [population_bp_mean, bootstrap_avg_bp],
        ["Population Mean BP", "Bootstrap Avg Mean BP"],
        reports_dir / "bootstrap_vs_population_bp_mean.png",
        "Bootstrap vs Population Mean Blood Pressure",
        "Mean BP",
    )


if __name__ == "__main__":
    main()
