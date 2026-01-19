import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def ensure_output_dir(output_dir: str):
    """
    Ensures that the given output directory exists.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def basic_overview(df: pd.DataFrame):
    """
    Displays basic information about the dataset.
    """
    print("🔹 Dataset Shape:")
    print(df.shape)

    print("\n🔹 Dataset Info:")
    print(df.info())

    print("\n🔹 Statistical Summary:")
    print(df.describe())


def plot_numerical_distributions(df: pd.DataFrame, output_dir: str, save=True):
    """
    Plots histograms for numerical features.
    """
    ensure_output_dir(output_dir)

    df.hist(figsize=(10, 6))
    plt.suptitle("Distribution of Numerical Features")

    if save:
        plt.savefig(
            os.path.join(output_dir, "numerical_distributions.png"),
            bbox_inches="tight"
        )

    plt.show()
    plt.close()


def plot_categorical_counts(df: pd.DataFrame, column: str, output_dir: str, save=True):
    """
    Plots count distribution for a categorical feature.
    """
    ensure_output_dir(output_dir)

    plt.figure(figsize=(6, 4))
    sns.countplot(x=column, data=df)
    plt.title(f"Count Plot of {column}")

    if save:
        plt.savefig(
            os.path.join(output_dir, f"{column}_countplot.png"),
            bbox_inches="tight"
        )

    plt.show()
    plt.close()


def detect_outliers(df: pd.DataFrame, output_dir: str, save=True):
    """
    Detects outliers using box plots.
    """
    ensure_output_dir(output_dir)

    numeric_df = df.select_dtypes(include="number")

    plt.figure(figsize=(8, 5))
    sns.boxplot(data=numeric_df)
    plt.title("Outlier Detection Using Box Plot")

    if save:
        plt.savefig(
            os.path.join(output_dir, "outliers_boxplot.png"),
            bbox_inches="tight"
        )

    plt.show()
    plt.close()


def correlation_heatmap(df: pd.DataFrame, output_dir: str, save=True):
    """
    Plots correlation heatmap for numerical features.
    """
    ensure_output_dir(output_dir)

    corr = df.select_dtypes(include="number").corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")

    if save:
        plt.savefig(
            os.path.join(output_dir, "correlation_heatmap.png"),
            bbox_inches="tight"
        )

    plt.show()
    plt.close()
