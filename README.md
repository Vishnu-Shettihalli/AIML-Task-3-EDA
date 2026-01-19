# Exploratory Data Analysis (EDA) – Iris Dataset

## Overview
This project focuses on performing Exploratory Data Analysis (EDA) to understand data patterns, feature behavior, and relationships before applying machine learning models.

The goal was not just to generate plots, but to learn **how and why** each EDA step is performed.

---

## Dataset
**Iris Dataset**
- Contains flower measurements and species labels
- Clean dataset with no missing values
- Ideal for learning core EDA concepts

---

## Tools & Environment
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code
- Jupyter Notebook

---


## Learning Approach

### Step 1: Understanding the Dataset
- Loaded dataset using Pandas
- Used `.info()`, `.shape()`, and `.describe()` to understand structure and statistics

### Step 2: Visualizing Numerical Features
- Used histograms to analyze data distribution
- Identified which features show better separation

### Step 3: Analyzing Categorical Data
- Used count plots to verify class balance
- Confirmed equal distribution across species

### Step 4: Outlier Detection
- Used box plots to identify extreme values
- Learned how outliers can impact models

### Step 5: Correlation Analysis
- Used heatmaps to understand feature relationships
- Identified multicollinearity between petal features

---

## Custom EDA Module (`eda_utils.py`)
A reusable EDA utility module was created to:
- Encapsulate EDA logic into functions
- Improve code readability and maintainability
- Reflect professional data analysis workflows

Functions include:
- Dataset overview
- Distribution plots
- Count plots
- Outlier detection
- Correlation heatmap

---

## Automated Plot Saving
All visual outputs are automatically saved into the `outputs/` directory in PNG format.  
This ensures:
- Reproducibility
- Organized results
- Easy sharing and documentation

---

## Key Insights
- Dataset is clean and balanced
- Petal features are highly informative
- Visualization simplifies understanding of data behavior
- Correlation analysis helps identify multicollinearity

---

## What I Learned
- Importance of EDA before modeling
- How to interpret visual patterns
- Writing reusable and modular Python code
- Professional project structuring
- Debugging and improving real-world code issues

---

## Outcome
This project helped build a strong foundation in data analysis and improved both analytical and software development skills, preparing me for real-world AIML tasks.

## Netflix Dataset EDA
The same EDA pipeline was extended to the Netflix Movies and TV Shows dataset.
Additional steps included:
- Handling missing categorical values
- Feature engineering on duration
- Analysis of content type and ratings
This demonstrated the scalability of the custom EDA module.


