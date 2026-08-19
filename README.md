# Categorical Encoding Demo (Label Encoding vs One-Hot Encoding)

Chote se student dataset pe dikhaya gaya hai ki text (categorical) columns ko
ML-ready numbers mein kaise convert karte hain — do popular tarike se.

## Dataset

`sample_data.csv` — 10 students ka data:

| Column | Description |
|--------|-------------|
| Name   | Student name |
| Gender | Male / Female |
| Age    | Age in years |
| Passed | Yes / No (exam result) |

## What this script does

**1. Label Encoding** (`sklearn.preprocessing.LabelEncoder`)
- Har category ko ek integer number de deta hai — e.g. `Female → 0`, `Male → 1`
- Simple aur memory-efficient, lekin **ordinal relationship imply karta hai**
  (model soch sakta hai 1 > 0, jo yaha meaningless hai)
- Best suited for columns jaha order genuinely matter karta hai
  (e.g. `Low < Medium < High`)

**2. One-Hot Encoding** (`pandas.get_dummies`)
- Har category ke liye alag 0/1 column banata hai — e.g. `Gender_Male`, `Gender_Female`
- Koi false ordering nahi create hoti, isliye **nominal categories**
  (jaha koi natural order nahi hai) ke liye ye better choice hai
- Trade-off: zyada categories hone par columns badh jaate hain (dimensionality)

## Files

```
categorical-encoding-demo/
├── encode_demo.py      # main script
├── sample_data.csv      # sample dataset
├── requirements.txt     # dependencies
└── README.md
```

## How to run

```bash
pip install -r requirements.txt
python encode_demo.py
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

---
Built as part of Python/ML self-study — data preprocessing basics.# Categorical-Encoding-Demo-
