from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("sample_data.csv")
df_label = df.copy()

le=LabelEncoder()

df_label['Gender_Encoded'] = le.fit_transform(df_label['Gender'])
df_label['Passed_Encoded'] = le.fit_transform(df_label['Passed'])

print("\n label encode data")
print(df_label[['Name','Gender','Gender_Encoded','Passed','Passed_Encoded']])
print(df_label.head())

# columns to be one-hot encoded 0/1 bana sakta hai  

df_encoded = pd.get_dummies(df, columns=['Gender'])
print("\n onehot encode data")
print(df_encoded.head())
