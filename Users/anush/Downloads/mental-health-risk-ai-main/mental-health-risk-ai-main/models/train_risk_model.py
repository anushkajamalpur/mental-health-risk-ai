import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("data/risk_training.tsv", sep="\t")

X = df.drop("risk", axis=1)
y = df["risk"]

model = LogisticRegression(max_iter=2000)
model.fit(X, y)

model_path = os.path.join("models", "risk_model.pkl")
joblib.dump(model, model_path)

print("Risk model trained successfully at:", model_path)