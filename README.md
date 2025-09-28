# MAGIC Gamma Telescope Classification

This project uses the MAGIC Gamma Telescope dataset to classify events
as either gamma rays or hadrons.

## Overview

The script performs the following steps: 1. **Data Loading**: Reads the
dataset and assigns column names. 2. **Preprocessing**: - Converts class
labels (`g` → 1 for gamma, `h` → 0 for hadron). - Scales features using
`StandardScaler`. - Handles class imbalance with `RandomOverSampler`
(optional). 3. **Visualization**: Generates histograms to compare gamma
and hadron distributions for each feature. 4. **Data Splitting**:
Shuffles and splits the dataset into training, validation, and test sets
(60/20/20). 5. **Model Training**: Trains a K-Nearest Neighbors
classifier (k=5). 6. **Evaluation**: Uses the test set to generate
predictions and prints a classification report.

## Requirements

-   Python 3.x\
-   NumPy\
-   Pandas\
-   Matplotlib\
-   Scikit-learn\
-   Imbalanced-learn

Install dependencies with:

``` bash
pip install -r requirements.txt
```

## Usage

1.  Place the MAGIC dataset file (`magic04.data`) inside the
    `magic+gamma+telescope/` directory.\
2.  Run the script:

``` bash
python magic.py
```

3.  The script will output class distributions, plots, and a
    classification report.

## Output Example

-   Feature distribution plots (gamma vs. hadron).\
-   Classification report including precision, recall, and F1-score.

------------------------------------------------------------------------
