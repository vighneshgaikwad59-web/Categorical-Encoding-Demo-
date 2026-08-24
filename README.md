# Categorical Encoding Demo (Label Encoding vs One-Hot Encoding)

A small demo using a sample student dataset to show two common ways of
converting categorical (text) columns into numbers that machine learning
models can use.

## Dataset

`sample_data.csv` — data for 10 students:

| Column | Description |
|--------|-------------|
| Name   | Student name |
| Gender | Male / Female |
| Age    | Age in years |
| Passed | Yes / No (exam result) |

## What this script does

**1. Label Encoding** (`sklearn.preprocessing.LabelEncoder`)
- Assigns each category an integer — e.g. `Female → 0`, `Male → 1`
- Simple and memory-efficient, but it **implies an ordinal relationship**
  (the model may treat 1 as "greater than" 0, which is meaningless here)
- Best suited for columns where order genuinely matters
  (e.g. `Low < Medium < High`)

**2. One-Hot Encoding** (`pandas.get_dummies`)
- Creates a separate 0/1 column for each category — e.g. `Gender_Male`, `Gender_Female`
- Doesn't introduce any false ordering, so it's the better choice for
  **nominal categories** (ones with no natural order)
- Trade-off: more categories means more columns (higher dimensionality)

## Files

```
categorical-encoding-demo/
├── encode_demo.py      # main script
├── sample_data.csv      # sample dataset
├── requirements.txt     # dependencies
└── README.md
```


## Sample output

```
Gender mapping: {'Female': 0, 'Male': 1}
Passed mapping: {'No': 0, 'Yes': 1}
```

## When to use which

| Situation | Use |
|-----------|-----|
| Categories have a natural order (Low/Medium/High) | Label Encoding |
| Categories have no order (Gender, City, Color) | One-Hot Encoding |
| Tree-based models (Random Forest, XGBoost) | Label Encoding often works fine |
| Linear models / Neural Nets, no ordinal columns | One-Hot Encoding preferred |

